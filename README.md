# Exercise-03

Suitable for intermediate level students who are familiar with classes and data structures including queues, and are learning about unit testing and error handling.

## Exchange

An exchange is responsible for managing all client connections, handling incoming order operation requests (i.e. insert order, delete order), and executing trades when inserted orders are in cross. Two orders are in cross if they have opposing sides and the buy price is greater than or equal to the sell price. Let’s revisit the order book from Exercise-02 to see how price time priority applied when matching orders.
```
                                   60c     James:20
                                   55c     Nicky:10, Tim:10
                                   50c
               Tim:10, Nicky:10    45c
                       James:20    40c
```
If I was prepared to sell 30 apples at 40c each, then I would that sell order resulting in the following three trades:

 1. Nicky would get to buy her 10 from me first at 45c each.
 1. Tim buys his 10 from me next, also at 45c each.
 1. Finally, James buys the remaining 10 from me at 40c each.

Once those three trades have occurred, the order book will look like this:
```
                                   60c     James:20
                                   55c     Nicky:10, Tim:10
                                   50c
                                   45c
                       James:10    40c
```
We will also have a new entity called a trade list that keeps track of all the matched orders resulting in trades:
```
Nicky B 45@10 Kim
Tim   B 45@10 Kim
James B 40@10 Kim
```

## Instructions

- Checkout this branch (refer to the tips on the master branch if you are new to using git):
```
git checkout exercise-03
```
 - The branch includes an incomplete implementation of an Exchange class provided in market/exchange.py.
 - Unit tests describing how the Exchange class should behave are in test/test_exchange.py.
 - Some additional classes that the Exchange will need -- including Side, Order, Trade, and Client -- are in market/markettypes.py.
 - Run the unit tests, most of which will be failing (refer to the tips on the master branch if you are new to running Python unit tests):
```
python -m unittest discover
```
 - Your task is to complete each empty function in the Exchange class by replacing `pass` with the code that will carry out the behaviour described in the function comment  until **all unit tests are passing**. For example, the `handle_login_request` function will need to create a new Client object using the provided name, add it to the `self._clients` dictionary, and return the client ID:
```
    def handle_login_request(self, name):
        """
        Create a new Client using the specified name, and return the clientid.
        """
        pass
```
 - You will know that you have completed this exercise when your output looks like this:
```
.......................
----------------------------------------------------------------------
Ran 35 tests in 0.004s

OK
```

## Extensions

Try these exercises if you want more of a challenge!

### Order Lifespan
Our exchange only caters for Good For Day (GFD) orders, meaning any unmatched order volume will rest in the order book until it is traded or deleted. However, there is another standard Fill And Kill (FAK) order type that allows the client to insert an order which will not be inserted into the order book if it does not trade.

 - Add a new Lifespan enumerated market type allowing GFD and FAK.
 - Extend the Order class to include a life span attribute.
 - Extend the Exchange class to cater for both types of orders.
 - Add and amend unit tests as required for this new functionality.

### Multiple Instruments
The sample code provided only caters for a single instrument on our exchange.

 - Add a new market type describing instruments.
 - Extend the Exchange class to cater for one order book per instrument.
 - Add and amend unit tests as required for this new functionality.