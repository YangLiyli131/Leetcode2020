class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}       
        self.prex = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.m[key] = val
        self.prex[key] = []
        for i in range(1,len(key)+1):
            curs = key[:i]
            self.prex[key].append(curs)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        res = 0
        for k in self.m:
            if prefix in self.prex[k]:
                res += self.m[k]
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)