class Solution(object):
    def heapsort(self, n):
        h = []
        for i in n:
            heappush(h,i)
        r = [heappop(h) for i in range(len(h))]
        res = []
        for h in r:
            res.insert(0,h)
        return res
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        x = self.heapsort(stones)
        while len(x) > 1:
            #print(x)
            a = x.pop(0)
            b = x.pop(0)
            if a != b:
                heappush(x, a-b)
            x = self.heapsort(x)
        if len(x) == 0:
            return 0
        return x[0]