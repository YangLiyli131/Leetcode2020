class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.arr = [''] * n
        self.pt = 1

    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        self.arr[id-1] = value
        res = []
        if self.pt == id:
            idx = id-1
            while idx < len(self.arr) and self.arr[idx] != '':
                res.append(self.arr[idx])
                idx += 1
            self.pt = idx+1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)