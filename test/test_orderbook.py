import unittest

from textmarket.markettypes import Side, Order
from textmarket.orderbook import OrderBook

class TestOrderBook(unittest.TestCase):

    def test_new_order_book_is_empty(self):
        ob = OrderBook()
        self.assertEquals(ob.buys().size(), 0)
        self.assertEquals(ob.sells().size(), 0)

    def test_insert_buy_order(self):
        ob = OrderBook()
        buy = Order(0, Side.BUY, 4.5, 10)
        
        ob.insert(buy)
        self.assertEquals(ob.buys().size(), 1)
        self.assertEquals(ob.buys().peek(), buy)

    def test_insert_sell_order(self):
        ob = OrderBook()
        sell = Order(0, Side.SELL, 7.5, 10)
        
        ob.insert(sell)
        self.assertEquals(ob.sells().size(), 1)
        self.assertEquals(ob.sells().peek(), sell)
        
    def test_cannot_insert_same_order_twice(self):
        """
        The same instance of an order may not be inserted more than once.
        However, multiple orders with the same attributes may be inserted.
        """
        ob = OrderBook()
        b1 = Order(0, Side.BUY, 4.5, 10)
        b2 = Order(0, Side.BUY, 4.5, 10)
        
        ob.insert(b1)
        self.assertRaises(AssertionError, ob.insert, b1)

        ob.insert(b2)
        self.assertEquals(ob.buys().size(), 2)

    def test_delete_buy_order(self):
        ob = OrderBook()
        buy = Order(0, Side.BUY, 4.5, 10)
        
        ob.insert(buy)
        ob.delete(buy.orderid)
        self.assertEquals(ob.buys().size(), 0)

    def test_delete_sell_order(self):
        ob = OrderBook()
        sell = Order(0, Side.SELL, 7.5, 10)
        
        ob.insert(sell)
        ob.delete(sell.orderid)
        self.assertEquals(ob.sells().size(), 0)
        
    def test_delete_order_not_in_book(self):
        """
        The client may try to remove an order that is not in the book without
        resulting in an error.
        """
        ob = OrderBook()
        ob.delete(Order(0, Side.BUY, 4.5, 10))

    def test_buy_prices(self):
        """
        Buy prices will be listed from most to least expensive.
        """
        ob = OrderBook()
        ob.insert(Order(0, Side.BUY, 4.0, 10))
        ob.insert(Order(0, Side.BUY, 5.0, 10))
        ob.insert(Order(0, Side.BUY, 4.5, 10))
        self.assertItemsEqual(ob.prices(Side.BUY), [5.0, 4.5, 4.0])

    def test_sell_prices(self):
        """
        Buy prices will be listed from least to most expensive.
        """
        ob = OrderBook()
        ob.insert(Order(0, Side.SELL, 7.0, 10))
        ob.insert(Order(0, Side.SELL, 8.0, 10))
        ob.insert(Order(0, Side.SELL, 7.5, 10))
        self.assertItemsEqual(ob.prices(Side.SELL), [7.0, 7.5, 8.0])

    def test_buys_price_time_priority(self):
        """
        Buy orders will be listed first by price (most to least expensive),
        and then by time priority (the order in which they were inserted).
        """
        ob = OrderBook()
        b1 = Order(0, Side.BUY, 4.0, 10)
        b2 = Order(0, Side.BUY, 4.5, 10)
        b3 = Order(0, Side.BUY, 4.5, 10)

        ob.insert(b1)
        ob.insert(b2)
        ob.insert(b3)
        self.assertItemsEqual(ob.buys().items(), [b2, b3, b1])

    def test_sells_price_time_priority(self):
        """
        Sell orders will be listed first by price (least to most expensive),
        and then by time priority (the order in which they were inserted).
        """
        ob = OrderBook()
        s1 = Order(0, Side.SELL, 7.0, 10)
        s2 = Order(0, Side.SELL, 7.5, 10)
        s3 = Order(0, Side.SELL, 7.5, 10)
        
        ob.insert(s3)
        ob.insert(s2)
        ob.insert(s1)
        self.assertItemsEqual(ob.sells().items(), [s1, s3, s2])
