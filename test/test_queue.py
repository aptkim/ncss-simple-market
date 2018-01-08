import unittest

from textmarket.queue import Queue

class TestQueue(unittest.TestCase):

    def test_size_when_empty(self):
        q = Queue()
        self.assertEqual(q.size(), 0)

    def test_size_when_has_items(self):
        q = Queue([1, 2, 3])
        self.assertEqual(q.size(), 3)

    def test_peek_does_not_remove(self):
        q = Queue([23, 14])
        self.assertEqual(q.peek(), 23)
        self.assertEqual(q.size(), 2)

    def test_dequeue_from_empty_queue(self):
        q = Queue()
        self.assertEqual(q.dequeue(), None)

    def test_dequeue_from_front_of_queue(self):
        q = Queue([10, 20, 30])
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.peek(), 20)
        self.assertEqual(q.size(), 2)

    def test_enqueue_to_empty_queue(self):
        q = Queue()
        q.enqueue(10)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.peek(), 10)

    def test_enqueue_to_back_of_queue(self):
        q = Queue([10, 20, 30])
        q.enqueue(40)
        self.assertEqual(q.size(), 4)
        self.assertNotEqual(q.peek(), 40)
