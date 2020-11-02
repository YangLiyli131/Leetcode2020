class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.arr = []
        self.cap = 0
        self.total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.cap < self.size:
            self.arr.append(val)
            self.total += val
            self.cap += 1
            return self.total / float(self.cap)
        else:
            x = self.arr.pop(0)
            self.arr.append(val)
            self.total = self.total - x + val
            return self.total / float(self.cap)
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)