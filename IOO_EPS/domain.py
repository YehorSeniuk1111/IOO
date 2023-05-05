import datetime


class Payment:

    def __init__(self, amount: int):
        self.amount = amount


class ProductSpecification:

    def __init__(self, ps_id, item_id: str, price: float, description: str):
        self.id = ps_id
        self.description = description
        self.price = price
        self.item_id = item_id


class ProductCatalog:

    @staticmethod
    def get_specification(item_id: str):
        from storage import PersistenceFacade
        ps = PersistenceFacade()
        return ps.get(item_id, ProductSpecification)


class SalesLineItem:

    def __init__(self, spec: ProductSpecification, quantity: int):
        self.quantity = quantity
        self.spec = spec

    def get_subtotal(self):
        return self.spec.price * self.quantity


class Sale:

    def __init__(self, user_id):
        self.line_items = []
        self.datetime = datetime.datetime.now()
        self.is_complete = False
        self.payment = None
        self.property_listeners = []
        self.account_id = user_id

    def become_complete(self):
        self.is_complete = True

    def make_line_item(self, spec: ProductSpecification, quantity: int):
        self.line_items.append(SalesLineItem(spec, quantity))
        self.publish_property_event('sale.new_item', f'{spec.description} x{quantity} шт. {round(spec.price * quantity, 2)} грн')

    def make_payment(self, amount: int):
        self.payment = amount
        self.publish_property_event('sale.payed', f'Сплачено {amount} грн')
        self.publish_property_event('sale.change', f'Решта {round(amount - self.get_total(), 2)} грн')
        from storage import PersistenceFacade
        ps = PersistenceFacade()
        ps.put(self)

    def get_total(self):
        s = 0
        for sli in self.line_items:
            s += sli.get_subtotal()
        s = round(s, 2)
        print(s)
        self.publish_property_event('sale.total', s)
        return s

    def delete_item(self, index):
        del self.line_items[index]
        self.get_total()

    def add_property_listener(self, property_listener):
        self.property_listeners.append(property_listener)

    def publish_property_event(self, name, value):
        for pl in self.property_listeners:
            pl.on_property_event(self, name, value)


class Account:

    def __init__(self, user_id, username, login, password):
        self.user_id = user_id
        self.username = username
        self.login = login
        self.password = password
        print(user_id)


class Register:

    def __init__(self, pc):
        self.s = None
        self.pc = pc
        self.account = None
        self.property_listeners = []

    def end_sale(self):
        self.s.become_complete()

    def enter_item(self, item_id: str, quantity: int):
        spec = self.pc.get_specification(item_id)
        self.s.make_line_item(spec, quantity)

    def make_new_sale(self):
        self.s = Sale(self.account.user_id)

    def make_payment(self, amount: float):
        self.s.make_payment(amount)

    def authorize(self, login, password):
        from storage import PersistenceFacade
        ps = PersistenceFacade()
        account = ps.authorize(login, password)
        if account is None:
            return None
        else:
            self.account = account
            return account.username

    def add_property_listener(self, property_listener):
        self.property_listeners.append(property_listener)

    def publish_property_event(self, name, value):
        for pl in self.property_listeners:
            pl.on_property_event(self, name, value)


class Store:

    def __init__(self):
        self.pc = ProductCatalog()
        self.register = Register(self.pc)
