import unittest

from textmarket.exchange import Exchange
from textmarket.markettypes import Client, Side, Order
from textmarket.orderbook import OrderBook

class TestExchange(unittest.TestCase):
    def setUp(self):
        self.exchange = Exchange()
        self.client1 = self.exchange.handle_login_request("client1")
        self.client2 = self.exchange.handle_login_request("client2")

    def test_client_must_login_to_insert_orders(self):
        """
        A client cannot insert orders until it has connected.
        """
        ex = Exchange()
        clientid = Client("client")
        self.assertRaises(RuntimeError, ex.handle_insert_request, clientid, Side.BUY, 4.5, 10)

    def test_client_must_login_to_logoff(self):
        """
        A client cannot disconnect unless it is connected.
        """
        ex = Exchange()
        clientid = Client("client")
        self.assertRaises(RuntimeError, ex.handle_logoff_request, clientid)

    def test_connected_client_insert_order(self):
        """
        Once a client has connected, it can insert an order that will rest in
        the order book until the order is matched or deleted.
        """
        ex, clientid = self.exchange, self.client1
        orderid = ex.handle_insert_request(clientid, Side.BUY, 4.5, 10)
        self.assertEqual(ex.order_book.buys().size(), 1)

        order = ex.order_book.buys().peek()
        self.assertEqual(order.orderid, orderid)
        self.assertIn(order, ex._clients[clientid].orders)

    def test_connected_client_delete_own_order(self):
        """
        Once a client has inserted an order, it can also delete it.
        """
        ex, clientid = self.exchange, self.client1
        orderid = ex.handle_insert_request(clientid, Side.BUY, 4.5, 10)
        ex.handle_delete_request(clientid, orderid)
        self.assertEqual(ex.order_book.buys().size(), 0)

    def test_client_cannot_delete_other_orders(self):
        """
        A client cannot delete orders that have been inserted by other clients.
        """
        ex, c1, c2 = self.exchange, self.client1, self.client2
        o1 = ex.handle_insert_request(c1, Side.BUY, 5.0, 10)
        o2 = ex.handle_insert_request(c2, Side.SELL, 7.0, 10)
        self.assertRaises(RuntimeError, ex.handle_delete_request, c2, o1)

    def test_disconnected_client_deletes_active_orders(self):
        """
        When a client disconnects, the exchange will delete any orders that it
        had inserted that still remain in the order book.
        """
        ex, clientid = self.exchange, self.client1
        o1 = ex.handle_insert_request(clientid, Side.BUY, 5.0, 10)
        o2 = ex.handle_insert_request(clientid, Side.SELL, 7.0, 10)
        self.assertEqual(len(ex.order_book._orders), 2)
        self.assertEqual(len(ex._clients[clientid].orders), 2)

        ex.handle_logoff_request(clientid)
        self.assertEqual(len(ex.order_book._orders), 0)
        self.assertNotIn(clientid, ex._clients)

    def test_insert_orders_not_in_cross_no_trade(self):
        """
        If inserted orders are not in cross, then they will rest in the order
        book until they are matched or deleted.
        """
        ex, c1, c2 = self.exchange, self.client1, self.client2
        o1 = ex.handle_insert_request(c1, Side.BUY, 5.0, 10)
        o2 = ex.handle_insert_request(c2, Side.SELL, 7.0, 10)
        self.assertEqual(len(ex.trades), 0)

    def test_insert_orders_in_cross_trade_and_removed_from_book(self):
        """
        If an inserted order exactly matches an order on the book, then it
        results in in a trade. Since there is no remaining volume on either
        side, there will be no orders remaining on the book afterwards.
        """
        ex, c1, c2 = self.exchange, self.client1, self.client2
        o1 = ex.handle_insert_request(c1, Side.BUY, 6.0, 10)
        o2 = ex.handle_insert_request(c2, Side.SELL, 6.0, 10)

        self.assertEqual(len(ex.trades), 1)
        self.assertEqual(ex.trades[0].buyer, ex._clients[c1])
        self.assertEqual(ex.trades[0].seller, ex._clients[c2])
        self.assertEqual(ex.trades[0].price, 6.0)
        self.assertEqual(ex.trades[0].volume, 10)

        self.assertEqual(ex.order_book.buys().size(), 0)
        self.assertEqual(ex.order_book.sells().size(), 0)

    def test_insert_orders_in_cross_favour_existing_buy_price(self):
        """
        If an inserted sell is priced below the best buy price in the order
        book, then the trade will favour the existing buy order.
        """
        ex, c1, c2 = self.exchange, self.client1, self.client2
        o1 = ex.handle_insert_request(c1, Side.BUY, 6.5, 10)
        o2 = ex.handle_insert_request(c2, Side.SELL, 6.0, 10)
        self.assertEqual(ex.trades[0].price, 6.5)

    def test_insert_orders_in_cross_favour_existing_sell_price(self):
        """
        If an inserted buy is priced above the best sell price in the order
        book, then the trade will favour the existing sell order.
        """
        ex, c1, c2 = self.exchange, self.client1, self.client2
        o1 = ex.handle_insert_request(c1, Side.SELL, 6.0, 10)
        o2 = ex.handle_insert_request(c2, Side.BUY, 6.5, 10)
        self.assertEqual(ex.trades[0].price, 6.0)

    def test_insert_orders_in_cross_remaining_volume_still_in_book(self):
        """
        If an inserted order has less volume than an existing matching order,
        than the existing order remains in the book, minus the traded volume.
        """
        ex, c1, c2 = self.exchange, self.client1, self.client2
        o1 = ex.handle_insert_request(c1, Side.BUY, 6.0, 10)
        o2 = ex.handle_insert_request(c2, Side.SELL, 6.0, 5)
        self.assertEqual(ex.trades[0].volume, 5)
        self.assertEqual(ex.order_book._orders[o1].volume, 5)

    def test_insert_orders_in_cross_excess_volume_inserted(self):
        """
        If an inserted order has more volume than an existing matching order,
        than the existing order trades and is removed from the book, and the
        new order is inserted minus the traded volume.
        """
        ex, c1, c2 = self.exchange, self.client1, self.client2
        o1 = ex.handle_insert_request(c1, Side.BUY, 6.0, 10)
        o2 = ex.handle_insert_request(c2, Side.SELL, 6.0, 15)
        self.assertEqual(ex.trades[0].volume, 10)
        self.assertEqual(ex.order_book._orders[o2].volume, 5)
