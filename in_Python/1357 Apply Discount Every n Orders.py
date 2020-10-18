class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.num = n
        self.discount = discount
        self.map = collections.defaultdict(int)
        for p in range(len(products)):
            self.map[products[p]] = prices[p]        
        self.count = 0

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        self.count += 1
        b = 0
        for i in range(len(product)):
            b += self.map[product[i]] * amount[i]
        if self.count % self.num == 0:
            return b - (b * self.discount / float(100) )
        else:
            return b
            

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)