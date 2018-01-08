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
        client = Client(name)
        self._clients[client.clientid] = client
        return client.clientid

    def handle_logoff_request(self, clientid):
        """
        Remove specified client from the exchange, and delete any outstanding
        orders belonging to that client from the order book.
        """
        if clientid not in self._clients:
            raise RuntimeError("Client is not logged in")
        
        client = self._clients.pop(clientid)
        for order in client.orders:
            self.order_book.delete(order.orderid)

    def handle_insert_request(self, clientid, side, price, volume):
        """
        Create a new Order using the specified clientid, side, price, and
        volume, and return the orderid. Attempt to match the new order to any
        existing orders in the order book, creating a trade for each match.
        If after trading there is volume remaining on the order, insert it
        into the order book.
        """
        if clientid not in self._clients:
            raise RuntimeError("Client is not logged in")
        
        order = Order(clientid, side, price, volume)
        client = self._clients[clientid]
        queue = self.order_book.buys() if order.side == Side.SELL else self.order_book.sells()

        while order.volume > 0 and queue.peek() and self._in_cross(queue.peek(), order):
            order2 = queue.dequeue()
            client2 = self._clients[order2.clientid]

            buyer, seller = (client, client2) if order.side == Side.BUY else (client2, client)
            trade = Trade(buyer, seller, order2.price, min(order.volume, order2.volume))
            order.volume -= trade.volume
            order2.volume -= trade.volume
            self.trades.append(trade)

            if order2.volume == 0:
                client2.orders.remove(order2)
                self.order_book.delete(order2.orderid)

        if order.volume > 0:
            self._clients[clientid].orders.append(order)
            self.order_book.insert(order)

        return order.orderid

    def handle_delete_request(self, clientid, orderid):
        """
        Remove the corresponding order from the order book, provided it was
        inserted by the requesting client.
        """
        if clientid not in self._clients:
            raise RuntimeError("Client is not logged in")

        client = self._clients[clientid]
        order = [o for o in client.orders if o.orderid == orderid]
        if not order:
            raise RuntimeError("Order doesn't belong to client")

        client.orders.remove(order[0])
        self.order_book.delete(orderid)
    
    def _in_cross(self, order2, new_order):
        """
        Return True if new_order is in cross with order2, otherwise
        return False. Two orders are in cross if they have opposing sides and
        the buy price is greater than or equal to the sell price.
        """
        if order2.side == Side.BUY and new_order.side == Side.SELL:
            return order2.price >= new_order.price
        if order2.side == Side.SELL and new_order.side == Side.BUY:
            return order2.price <= new_order.price
        return False
