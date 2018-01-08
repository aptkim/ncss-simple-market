class Queue:
    def __init__(self, items=[]):
        self._queue = []
        for i in items:
            self.enqueue(i)

    def size(self):
        """
        Return the number of items currently in the queue.
        """
        return len(self._queue)

    def peek(self):
        """
        Return the item at the front of the queue without removing it.
        """
        if len(self._queue) == 0:
            return None
        return self._queue[0]

    def dequeue(self):
        """
        Remove and return the item at the front of the queue.
        """
        if len(self._queue) == 0:
            return None
        return self._queue.pop(0)

    def enqueue(self, item):
        """
        Insert the specified item at the back of the queue.
        """
        self._queue.append(item)

    def remove(self, item):
        """
        Remove the specified item from the queue without returning it.
        """
        self._queue.remove(item)

    def items(self, reverse=False):
        """
        Return a new list of the items in the queue.
        
        reverse is an optional argument with a boolean value. If set to False,
        the 0th item in the list is the front of the queue, and the nth item is
        the back of the queue. If set to True, the nth item is the front and
        the 0th is the back. The default value is False (0th is the front).
        """
        if not reverse:
            for item in self._queue:
                yield item
        else:
            for item in self._queue[::-1]:
                yield item
