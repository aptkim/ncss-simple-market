from datetime import datetime

class Side:
    BUY = 0
    SELL = 1

class Client:
    """
    A client is an exchange participant who places orders in the hopes that
    they will make a profitable trade.
    """
    def __init__(self, name):
        self.clientid = id(self)
        self.name = name
        self.orders = []
        
    def __str__(self):
        return "{self.name} ({self.clientid})".format(self=self)

class Order:
    """
    An order indicates that a client is prepared to buy or sell a certain
    number of contracts (volume) at a particular price.
    """
    def __init__(self, clientid, side, price, volume):
        assert side == Side.BUY or side == Side.SELL, "Side must be Side.BUY or Side.SELL"
        assert price >= 0, "Price must not be negative"
        assert volume >= 0, "Volume must not be negative"

        self.orderid = id(self)
        self.clientid = clientid
        self.side = side
        self.price = price
        self.volume = volume

    def __str__(self):
        side_str = "B" if self.side == Side.BUY else "S"
        return "{side} {self.price}@{self.volume}".format(side=side_str, self=self)

class Trade:
    """
    A trade is what occurs when two orders have been matched.
    """
    def __init__(self, buyer, seller, price, volume):
        self.tradeid = id(self)
        self.timestamp = datetime.now()
        self.buyer = buyer
        self.seller = seller
        self.price = price
        self.volume = volume

    def __str__(self):
        return "[{self.timestamp}] {self.buyer} {self.price}@{self.volume} {self.seller}".format(self=self)
