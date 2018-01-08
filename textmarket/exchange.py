from datetime import datetime

from markettypes import Side, Order, Trade, Client
from orderbook import OrderBook
from queue import Queue

class Exchange:
    def __init__(self):
        self._clients = {}
        self.trades = []
        self.order_book = OrderBook()

    def handle_login_request(self, name):
        """
        Create a new Client using the specified name, and return the clientid.
        """
        pass

    def handle_logoff_request(self, clientid):
        """
        Remove specified client from the exchange, and delete any outstanding
        orders belonging to that client from the order book.
        """
        pass

    def handle_insert_request(self, clientid, side, price, volume):
        """
        Create a new Order using the specified clientid, side, price, and
        volume, and return the orderid. Attempt to match the new order to any
        existing orders in the order book, creating a trade for each match.
        If after trading there is volume remaining on the order, insert it
        into the order book.
        """
        pass

    def handle_delete_request(self, clientid, orderid):
        """
        Remove the corresponding order from the order book, provided it was
        inserted by the requesting client.
        """
        pass
    
    def _in_cross(self, order2, new_order):
        """
        Return True if new_order is in cross with order2, otherwise
        return False. Two orders are in cross if they have opposing sides and
        the buy price is greater than or equal to the sell price.
        """
        pass
