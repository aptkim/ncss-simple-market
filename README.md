# ncss-simple-market

This is an educational repository providing exercises for students of NCSS attending a master class run by sponsoring company Optiver. It is ideal for students who already have some Python programming skills, including a basic understanding of [classes](https://docs.python.org/3/tutorial/classes.html).

Each exercise is in a series of branches that continue to build upon each other to create a simple market, eventually allowing clients to connect and place orders which will result in trades.

Each branch has some background reading material and instructions relating to the lesson in the README.md file (which is what you're reading right now). Come back here to this README.md on the master branch for general tips to help you with the exercises.

The code for this class can run on any modern operating system including Windows, Mac OSX, and Linux. You will need Python (2.7+ or 3+) installed, some command line tool for checking out and running the code, and *any* text editor you like for modifying the code.

Popular command line tools for Windows are Cygwin and cmder. Mac OSX and Linux should have something like Terminal installed by default. The following sections provide instructions for checking out the code using **git** and running the Python **unit tests**.

## git

This master class is using [git](https://en.wikipedia.org/wiki/Git), a [version control](https://en.wikipedia.org/wiki/Version_control) system that is very popular amongst software developers, and one that you will use as part of your project at NCSS. It is a technology that enables us to view the history of changes to our code, and also allows multiple developers to work on the same code base at the same time by keeping a shared copy somewhere central for everyone to access, such as GitHub.

However, you don't need to know too much about git to use it for this master class, as you should be able to do everything you need using the commands below. If you would like to learn more about git, please see the Further Reading.

 - If you are retrieving the ncss-simple-market repository from GitHub for the first time:
```
git clone https://github.com/aptkim/ncss-simple-market.git
cd ncss-simple-market
```
 - Once you have cloned the ncss-simple-market repository from GitHub, switch to the branch corresponding to the exercise you would like to try:
```
git checkout exercise-01
```
 - If you have local changes from a previous exercise that are preventing you from checking out a different branch, you can commit them locally first (your changes will not appear on GitHub!):
```
git commit -a -m “My solutions to this exercise”
git checkout exercise-01
```
### Further Reading

 - https://git-scm.com/videos
 - https://git-scm.com/book/en/v2

## Python Unit Tests

A **[unit test](https://en.wikipedia.org/wiki/Unit_testing)** is a piece of code that is designed to test some small part of your project. As a simple example, if you have a Calculator class with an `add` function, you might write a test to ensure that when you call `add(2, 4)` that it returns 6. Once written, we have a repeatable and automated way of making sure all the small parts of our project are still working according to the specification.

**[Test driven development](https://en.wikipedia.org/wiki/Test-driven_development)** is a style of writing code where the unit tests are written *first* and can serve as a specification for your project. Once all the unit tests are passing, you can be confident that the specification has been met. This approach is used for some of the exercises for this master class. You will be asked to run all of the unit tests from the command line, and work on the incomplete implementation until the tests all pass.
```
python -m unittest discover
```
The output from running the unit tests will start with a line like this, which is using `.` to indicate a test that passed and `F` to indicate a test that failed:
```
.FFFF.FF
```
The output will continue with details of each failing test case. Here is an example of one of the failed test cases showing that the test `test_dequeue_from_front_of_queue` failed because it was expecting the operation `q.dequeue()` to return 10, but it instead returned `None`:
```
======================================================================
FAIL: test_dequeue_from_front_of_queue (test.test_queue.TestQueue)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/kim/Documents/repo/ncss-simple-market/test/test_queue.py", line 30, in test_dequeue_from_front_of_queue
    self.assertEqual(q.dequeue(), 10)
AssertionError: None != 10
```
The final line of the output will summarise the number of tests that ran, the overall result `FAILED` or `OK`, and a breakdown of the number of failures and errors:
```
----------------------------------------------------------------------
Ran 8 tests in 0.001s

FAILED (failures=6)
```

### Further Reading

 - https://docs.python.org/3/library/unittest.html