from queue import Queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.put(x);    
        i = 1;
        while i < self.stack.qsize():
            i += 1
            self.stack.put(self.stack.get())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.get()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        top = self.stack.get()
        self.push(top)
        return top
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stack.empty()