import unittest
from domain import *


class SaleTest(unittest.TestCase):
    acc = Account(1, 'Name Lastname', 'test@ioo.com', 'test_password')
    s = Sale(acc.user_id)

    def test_become_complete(self):
        self.assertFalse(self.s.is_complete)
        self.s.become_complete()
        self.assertTrue(self.s.is_complete)

    def test_make_line_item(self):
        spec = ProductSpecification(1, '123', 20.99, 'Test product')
        quantity = 2

        self.s.make_line_item(spec, quantity)
        line_item = self.s.line_items[-1]
        self.assertIn(line_item, self.s.line_items)

    def test_make_payment(self):
        pass

    def test_get_total(self):
        spec1 = ProductSpecification(1, '123', 20.99, 'Test product1')
        spec2 = ProductSpecification(2, '456', 2.50, 'Test product2')
        spec3 = ProductSpecification(3, '789', 9.99, 'Test product3')

        self.s.make_line_item(spec1, 3)
        self.s.make_line_item(spec2, 4)
        self.s.make_line_item(spec3, 9)

        self.assertEqual(self.s.get_total(), 162.88)

    def test_delete_item(self):
        spec1 = ProductSpecification(1, '123', 20.99, 'Test product1')
        spec2 = ProductSpecification(2, '456', 2.50, 'Test product2')
        spec3 = ProductSpecification(3, '789', 9.99, 'Test product3')
        index = 1

        self.s.make_line_item(spec1, 3)
        self.s.make_line_item(spec2, 4)
        self.s.make_line_item(spec3, 9)

        line_item0 = self.s.line_items[0]
        line_item1 = self.s.line_items[index]
        line_item2 = self.s.line_items[1]
        self.s.delete_item(index)

        self.assertIn(line_item0, self.s.line_items)
        self.assertNotIn(line_item1, self.s.line_items)
        self.assertIn(line_item2, self.s.line_items)

    def test_add_property_listener(self):
        pass


class RegisterTest(unittest.TestCase):
    pass


class SaleLineItemTest(unittest.TestCase):
    spec = ProductSpecification(1, '123', 20.99, 'Test product')
    sli = SalesLineItem(spec, 3)

    def test_get_subtotal(self):
        self.assertEqual(self.sli.get_subtotal(), 62.97)
