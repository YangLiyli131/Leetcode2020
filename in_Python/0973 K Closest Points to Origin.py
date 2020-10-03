class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        q = []
        qq = []
        for p in points:
            d = p[0] * p[0] + p[1] * p[1]
            heappush(q,(d,p))

        while len(qq) < K:
            heappush(qq,heappop(q))
        res = []
        while K != 0:
            res.append(heappop(qq)[1])
            K -= 1
        return res