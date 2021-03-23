class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.i1 = 0
        self.i2 = 0
        self.turn = 0      

    def next(self):
        """
        :rtype: int
        """
        if self.turn == 0:
            if self.i1 >= len(self.v1):
                r = self.v2[self.i2]
                self.i2 += 1
            else:
                r = self.v1[self.i1]
                self.i1 += 1
        else:
            if self.i2 >= len(self.v2):
                r = self.v1[self.i1]
                self.i1 += 1
            else:
                r = self.v2[self.i2]
                self.i2 += 1
        self.turn = 1 - self.turn
        return r
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i1 < len(self.v1) or self.i2 < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())