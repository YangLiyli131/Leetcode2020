class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.L = list()
        
    def seat(self):
        """
        :rtype: int
        """
        N, L = self.N, self.L
        if not self.L:
            res = 0
        else:
            d, res = L[0], 0
            for a,b in zip(L, L[1:]):
                if (b-a) / 2 > d:
                    res = (b+a) / 2
                    d = (b-a) / 2
            if N - 1 - L[-1] > d:
                res = N - 1
        bisect.insort(L, res)
        return res

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.L.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)