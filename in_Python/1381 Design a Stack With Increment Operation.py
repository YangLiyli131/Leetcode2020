class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.arr = []
        self.size = maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.arr) < self.size:
            self.arr.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        L = min(k, len(self.arr))
        for i in range(L):
            self.arr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)