import datetime
import sqlite3
from abc import ABC, abstractmethod
import pymysql
import pymysql.cursors

from domain import ProductSpecification, Account, Sale


class ExternalDataBase:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(ExternalDataBase, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect()
        self.success = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='',
                database='logisticsdb',
            )
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
            self.success = True
        except:
            self.success = False

    def get_last_id(self, table_name):
        try:
            last_id = self.cursor.execute(f'SELECT LAST_INSERT_ID() FROM {table_name}')
            self.success = True
            return last_id
        except:
            self.success = False

    def execute(self, command):
        try:
            self.cursor.execute(command)
            result = self.cursor.fetchall()
            self.connection.commit()
            self.success = True
            return result
        except Exception as e:
            self.success = False
            print(e)


class LocalDataBase:
    instance = None

    def __new__(cls, external_db):
        if cls.instance is None:
            cls.instance = super(LocalDataBase, cls).__new__(cls)
        return cls.instance

    def __init__(self, external_db: ExternalDataBase):
        self.turned_on = False
        self.external_db = external_db
        self.connection = None
        self.cursor = None
        self.connect()

    def get_last_id(self, table_name):
        last_id = self.external_db.get_last_id(table_name)
        if not self.external_db.success:
            self.turned_on = True
            last_id = self.cursor.execute(f'SELECT max(oid) FROM {table_name}').fetchone()[0]
            if last_id is None:
                last_id = 0
        else:
            if self.turned_on:
                self.turned_on = False
        return last_id

    def connect(self):
        self.connection = sqlite3.connect('local_db.db')
        self.cursor = self.connection.cursor()

    def synchronize(self):
        pass

    def execute(self, command):
        result = self.external_db.execute(command)
        if not self.external_db.success:
            print('Local')
            self.turned_on = True
            result = self.cursor.execute(command).fetchall()
            self.connection.commit()
            if result:
                columns = [columns[0] for columns in self.cursor.description]
                result = [dict(list(zip(columns, result[0])))]
        else:
            print('External')
            if self.turned_on:
                self.synchronize()
                self.turned_on = False
        return result



class IMapper(ABC):

    @abstractmethod
    def get(self, oid):
        pass

    @abstractmethod
    def put(self, obj):
        pass

class PersistenceFacade:

    def __init__(self):
        self.mappers = {ProductSpecification: ProductSpecificationRDBMapper('product_specification'),
                        Account: AccountRDBMapper('account'),
                        Sale: SaleRDBMapper('sale')}


    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(PersistenceFacade, cls).__new__(cls)
        return cls.instance

    def get(self, oid, cl):
        mapper = self.mappers[cl]
        return mapper.get(oid)

    def put(self, obj):
        mapper = self.mappers[type(obj)]
        mapper.put(obj)

    def authorize(self, login, password):
        account = self.get(login, Account)
        if account.password == password:
            return account
        else:
            return None


class AbstractPersistenceMapper(IMapper):

    def __init__(self):
        self.cashed_objects = {}

    def get(self, oid):
        obj = self.cashed_objects.get(oid)
        if obj is None:
            obj = self._get_object_from_storage(oid)
            self.cashed_objects.update({oid: obj})
        return obj

    def put(self, obj):
        self._put_object_to_storage(obj)

    def _get_object_from_storage(self, oid):
        pass

    def _put_object_to_storage(self, obj):
        pass


class AbstractRDBMapper(AbstractPersistenceMapper):

    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name
        self.db = LocalDataBase(ExternalDataBase())

    def _get_object_from_storage(self, oid):
        db_record = self._get_db_record(oid)
        return self._get_object_from_record(oid, db_record)

    def _get_db_record(self, oid):
        return self.db.execute(f'SELECT * FROM {self.table_name}')

    def _get_object_from_record(self, oid, db_record):
        pass

    def _put_object_to_storage(self, obj):
        db_record = self._get_record_from_object(obj)
        self._put_record(db_record)

    def _get_record_from_object(self, obj):
        pass

    def _put_record(self, db_record):
        pass


class ProductSpecificationRDBMapper(AbstractRDBMapper):

    def _get_object_from_record(self, oid, db_record):
        db_record = db_record[0]
        ps_id = db_record.get('id')
        item_id = db_record.get('item_id')
        price = db_record.get('price')
        description = db_record.get('description')
        ps = ProductSpecification(ps_id, item_id, price, description)
        return ps

    def _get_db_record(self, oid):
        return self.db.execute(f'SELECT * FROM {self.table_name} WHERE item_id="{oid}"')


class AccountRDBMapper(AbstractRDBMapper):

    def _get_object_from_record(self, oid, db_record):
        db_record = db_record[0]
        account_id = db_record.get('id')
        login = db_record.get('login')
        password = db_record.get('password')
        username = db_record.get('username')
        acc = Account(account_id, username, login, password)
        return acc

    def _get_db_record(self, oid):
        return self.db.execute(f'SELECT * FROM {self.table_name} WHERE login="{oid}"')


class SaleRDBMapper(AbstractRDBMapper):

    def __init__(self, table_name):
        super().__init__(table_name)
        self.sale_id = None

    def put(self, obj):
        self._put_object_to_storage(obj)
        slirdbmapper = SaleLineItemRDBMapper('sale_sli', self.sale_id)
        for sli in obj.line_items:
            slirdbmapper.put(sli)

    def _get_record_from_object(self, obj):
        self.sale_id = self.db.get_last_id(self.table_name) + 1
        dt = datetime.datetime.now()
        total = obj.get_total()
        change = obj.payment
        account_id = obj.account_id
        return {'sale_id': self.sale_id, 'datetime': dt, 'total': total, 'change': change, 'account_id': account_id}

    def _put_record(self, db_record):
        self.db.execute(f'INSERT INTO sale (`id`, `datetime`, `total`, `change`, `account_id`) values ('
                        f'{db_record["sale_id"]},'
                        f'"{db_record["datetime"]}",'
                        f' {db_record["total"]},'
                        f' {db_record["change"]},'
                        f' {db_record["account_id"]});')


class SaleLineItemRDBMapper(AbstractRDBMapper):

    def __init__(self, table_name, sale_id):
        super().__init__(table_name)
        self.sale_id = sale_id

    def _get_record_from_object(self, obj):
        spec_id = obj.spec.id
        quantity = obj.quantity
        slip = obj.get_subtotal()
        return {'sale_id': self.sale_id, 'spec_id': spec_id, 'quantity': quantity, 'slip': slip}

    def _put_record(self, db_record):
        self.db.execute('INSERT INTO sale_sli (`sale_id`, `spec_id`, `quantity`, `slip`) values ('
                        f'{db_record["sale_id"]},'
                        f' {db_record["spec_id"]},'
                        f' {db_record["quantity"]},'
                        f' {db_record["slip"]});')
