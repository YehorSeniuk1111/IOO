import unittest
from storage import *


class ExternalDataBaseTest(unittest.TestCase):

    def test_singleton(self):
        db1 = ExternalDataBase()
        db2 = ExternalDataBase()

        self.assertIs(db1, db2)


class LocalDataBaseTest(unittest.TestCase):

    def test_singleton(self):
        edb = ExternalDataBase()
        db1 = LocalDataBase(edb)
        db2 = LocalDataBase(edb)

        self.assertIs(db1, db2)


class PersistentFacadeText(unittest.TestCase):

    def test_singleton(self):
        ps1 = PersistenceFacade()
        ps2 = PersistenceFacade()

        self.assertIs(ps1, ps2)
