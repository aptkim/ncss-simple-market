from .markettypes import Side, Order
from .queue import Queue

class OrderBook:
    def __init__(self):
        """
        self._orders maps an order ID to the corresponding order object.
        self._buys maps a buy price to a Queue of buy orders at that price.
        self._sells maps a sell price to a Queue of sell orders at that price.
        """
        self._orders = {}
        self._buys = {}
        self._sells = {}

    def insert(self, order):
        """
        Insert the specified order into the order book, by adding it to the
        back of the queue for its side and price.
        """
        pass

    def delete(self, orderid):
        """
        Remove the specified order from the order book, if it exists,
        regardless of its place in the queue.
        """
        pass

    def prices(self, side):
        """
        Return a new list of the prices for the specified side of the book.

        side is a required argument. If set to Side.BUY, the prices will be
        sorted in descending order. If set to Side.SELL, the prices will be
        sorted in ascending order.
        """
        pass

    def buys(self):
        """
        Return a new Queue of all buy orders in the order book. The first item
        in the queue will have the highest price time priority, and the last
        item will have the lowest priority.

        Price time priority for buy orders is sorted firstly by price (most to
        least expensive) then time (least to most recently inserted).
        """
        pass

    def sells(self):
        """
        Return a new Queue of all sell orders in the order book. The first item
        in the queue will have the highest price time priority, and the last
        item will have the lowest priority.

        Price time priority for sell orders is sorted firstly by price (least
        to most expensive) then time (least to most recently inserted).
        """
        pass

    def _book_side(self, side):
        """
        Return the specified side of the order book.
        """
        if side == Side.BUY:
            return self._buys
        return self._sells
