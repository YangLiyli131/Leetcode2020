class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1 = []
        self.st2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.st1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.st1) != 0:
            self.st2.append(self.st1.pop())
        a = self.st2.pop()
        while len(self.st2) != 0:
            self.st1.append(self.st2.pop())
        return a
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while len(self.st1) != 0:
            self.st2.append(self.st1.pop())
        b = self.st2[-1]
        while len(self.st2) != 0:
            self.st1.append(self.st2.pop())
        return b
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.st1) == 0 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()