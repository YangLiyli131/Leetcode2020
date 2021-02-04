class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.arr = []
        for x in v:
            for y in x:
                self.arr.append(y)
        self.id = 0

    def next(self):
        """
        :rtype: int
        """
        p = self.arr[self.id]
        self.id += 1
        return p

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.id <= len(self.arr)-1


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()