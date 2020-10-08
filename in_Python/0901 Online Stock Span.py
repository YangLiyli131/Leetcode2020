class StockSpanner(object):

    def __init__(self):
        self.st = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        while len(self.st) != 0 and self.st[-1][0] <= price:
            res += self.st.pop()[1]
        self.st.append([price,res])
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)