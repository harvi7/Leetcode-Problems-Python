class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._peeked_element = None
        self.hasPeeked = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.hasPeeked:
            self._peeked_element = self._iterator.next();
            self.hasPeeked = True
        return self._peeked_element

    def next(self):
        """
        :rtype: int
        """
        if not self.hasPeeked:
            return self._iterator.next()
        i = self._peeked_element
        self.hasPeeked = False
        return i;

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.hasPeeked or self._iterator.hasNext();