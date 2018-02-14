import unittest

from textmarket.markettypes import Side, Order

class TestOrder(unittest.TestCase):

    def test_orderid(self):
        """
        Order.orderid will be unique for each instance, even if they are otherwise identical.
        """
        o1 = Order(0, Side.BUY, 4.5, 10)
        o2 = Order(0, Side.BUY, 4.5, 10)
        self.assertNotEqual(o1.orderid, o2.orderid)

    def test_side(self):
        """
        Order.side must be either Side.BUY or Side.SELL.
        """
        o1 = Order(0, Side.BUY, 4.5, 10)
        o2 = Order(0, Side.SELL, 4.5, 10)
        self.assertEqual(o1.side, Side.BUY)
        self.assertEqual(o2.side, Side.SELL)
        self.assertRaises(AssertionError, Order, 0, -1, 4.5, 10)

    def test_price(self):
        """
        Order.price must not be negative.
        """
        o1 = Order(0, Side.BUY, 4.5, 10)
        o2 = Order(0, Side.BUY, 0.0, 10)
        self.assertEqual(o1.price, 4.5)
        self.assertEqual(o2.price, 0.0)
        self.assertRaises(AssertionError, Order, 0, Side.BUY, -4.5, 10)

    def test_volume(self):
        """
        Order.volume must not be negative.
        """
        o1 = Order(0, Side.BUY, 4.5, 10)
        o2 = Order(0, Side.BUY, 4.5, 0)
        self.assertEqual(o1.volume, 10)
        self.assertEqual(o2.volume, 0)
        self.assertRaises(AssertionError, Order, 0, Side.BUY, 4.5, -10)
