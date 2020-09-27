class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.minv = sys.maxint 
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x <= self.minv:
            self.arr.append(self.minv)
            self.minv = x
        self.arr.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.arr.pop() == self.minv:
            self.minv = self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minv
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()