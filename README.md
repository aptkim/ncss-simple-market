# Exercise-01

Suitable for beginner level students who are learning about classes and data structures.

## Queues

You are probably already familiar with some of the built-in collection types in Python, such as lists, sets, and dictionaries. They’re all designed to hold multiple items, but have different characteristics in how they behave, such as the ordering of items, uniqueness, and how you can access the items.
A FIFO (first in, last out) queue describes a collection where the order of items must be preserved, and items are added to the back of the queue (‘enqueue’, ‘push’, or ‘put’) and removed from the front (‘dequeue’, ‘pop’, or ‘get’). We will need to use queues in order to build our order book.

![Representation of a FIFO (first in, first out) queue](https://upload.wikimedia.org/wikipedia/commons/5/52/Data_Queue.svg)

You can read more about queues on Wikipedia: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)

## Instructions

 - Checkout this branch (refer to the tips on the master branch if you are new to using git):
```
git checkout exercise-01
```
 - The branch includes an incomplete implementation of a Queue class in market/queue.py, and some unit tests describing how the Queue should behave are in test/test_queue.py.
 - Run the unit tests, most of which will be failing (refer to the tips on the master branch if you are new to running Python unit tests):
```
python -m unittest discover
```
 - Your task is to complete each empty function in the Queue class by replacing `pass` with the code that will carry out the behaviour described in the function comment  until **all unit tests are passing**. For example, the `dequeue` class will need to remove and return the item at the front of the queue (`self._queue`):
```
    def dequeue(self):
        """
        Remove and return the item at the front of the queue.
        """
        pass
```
 -  You will know that you have completed this exercise when your output looks like this:
```
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```