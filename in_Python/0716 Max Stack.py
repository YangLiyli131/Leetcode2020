class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.maxval = -sys.maxint - 1       

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x >= self.maxval:
            self.st.append(self.maxval)
            self.maxval = x
        self.st.append(x)

    def pop(self):
        """
        :rtype: int
        """
        y = self.st.pop()
        if y == self.maxval:
            self.maxval = self.st.pop()
        return y
    
    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.maxval

    def popMax(self):
        """
        :rtype: int
        """
        newst = []
        while self.st[-1] < self.maxval:
            newst.append(self.st.pop())
        r = self.st.pop()
        self.maxval = self.st.pop()
        while newst:
            xx = newst.pop()
            if xx >= self.maxval:
                self.st.append(self.maxval)
                self.maxval = xx
            self.st.append(xx)
        return r


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()