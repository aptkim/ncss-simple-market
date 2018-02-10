# Exercise-02

Suitable for intermediate level students who are familiar with classes and data structures including queues.

## Order Book

An order describe the **price** and **quantity** that an exchange client would like to **buy** or **sell** at for a particular type of tradable contract, such as a stock (GOOG, RIO, CBA) or a commodity (oil, gold, soymeal), known as an **instrument**.

Generally speaking, clients will try to “buy low” and “sell high” in order obtain what they think is a good deal. For example, if you can buy apples from the fruit market for 50c each, then it would be a good deal if you could buy similar apples from your neighbour for 40c each. Conversely, if you had apples to sell and your neighbour was prepared to pay you 60c per apple, this would also be a good deal!

An **order book** is a list of all current orders that have been submitted by exchange clients for a single instrument. Typically there will be several orders to buy at lower prices and several orders to sell at higher prices. The highest buy price is known as the **best buy** or **bid**, and the lowest sell price is known as the **best sell** or **ask**. A trade will only occur once two parties have agreed on a price, which will be covered in Exercise-03.

If James and Nicky have both inserted buy and sell orders for some number of apples, then a textual representation of the order book might look something like this:
```
                                   60c     James:20
                                   55c     Nicky:10
                                   50c
                       Nicky:10    45c
                       James:20    40c
```
In this example, Nicky is quoting better prices to the market, and James is quoting for larger volume. If Tim came along and decided to copy Nicky’s orders, then after he inserts his two orders, the order book would look like this:
```
                                   60c     James:20
                                   55c     Nicky:10, Tim:10
                                   50c
               Tim:10, Nicky:10    45c
                       James:20    40c
```
When matching orders, priority is given to the best price, followed by the order at the front of the queue for that price. This is called **price time priority**.

## Instructions

 - Checkout this branch (refer to the tips on the master branch if you are new to using git):
```
git checkout exercise-02
```
 - The branch includes an incomplete implementation of an OrderBook class provided in textmarket/orderbook.py.
 - Unit tests describing how the OrderBook class should behave are in test/test_orderbook.py.
 - Some additional classes that the OrderBook will need -- including Order and Side -- are in test/test_markettypes.py.
 - Run the unit tests, most of which will be failing (refer to the tips on the master branch if you are new to running Python unit tests):
```
python -m unittest discover
```
 - Your task is to complete each empty function in the OrderBook class by replacing `pass` with the code that will carry out the behaviour described in the function comment  until **all unit tests are passing**. For example, the `insert` class will need to insert the specified order into the order book:
```
    def insert(self, order):
        """
        Insert the specified order into the order book, by adding it to the
        back of the queue for its side and price.
        """
        pass
```
 - For this example, you will need to use `order.side` to choose one of the two dictionaries `self._buys` or `self._sells`, and then use `order.price` to fetch (or create, if it doesn't yet exist) the correct Queue for the order. Once you have the Queue you can use its `enqueue` function to insert the order.
 - You will know that you have completed this exercise when your output looks like this:
```
.......................
----------------------------------------------------------------------
Ran 23 tests in 0.004s

OK
```

## Hints

- If you feel like you are duplicating code to do the same actions on either `self._buys` or `self._sells`, use the `_get_book_side` helper function:
```
book_side = self._book_side(order.side)
```
