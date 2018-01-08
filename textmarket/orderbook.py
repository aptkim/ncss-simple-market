from markettypes import Side, Order
from queue import Queue

class OrderBook:
    def __init__(self):
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
        pass

    def __str__(self):
        """
        Return a string representation of the order book, with prices ordered
        vertically down the middle from most to least expensive, with sells on
        the right side ordering oldest to newest from left to right, and
        buys on the left side ordering oldest to newest from right to left.
        
        Example:

                                          7.5     4323054728:10
                                          7.0     4323054800:20, 4323054872:10
          4323054584:20, 4323054368:10    4.5    
                         4323054656:15    4.0    
        """
        s = []
        for i in sorted(self._sells, reverse=True):
            order_str = ["{0.orderid}:{0.volume}".format(order) for order in self._sells[i].items()]
            s.append("{0:50} {price:^10} {orders}".format("", price=i, orders=", ".join(order_str)))
        for i in sorted(self._buys, reverse=True):
            order_str = ["{0.orderid}:{0.volume}".format(order) for order in self._buys[i].items(reverse=True)]
            s.append("{orders:>50} {price:^10}".format(price=i, orders=", ".join(order_str)))
        return "\n".join(s) + "\n"
