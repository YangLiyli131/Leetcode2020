class ProductOfNumbers(object):

    def __init__(self):
        self.num = []
        self.mul = 1

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num != 0:
            self.mul *= num
            self.num.append(self.mul)
        else:
            self.num = []
            self.mul = 1
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k > len(self.num):
            return 0
        elif k == len(self.num):
            return self.num[-1]
        else:
            return self.num[-1] / self.num[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)