class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        idx = []
        for i,s in enumerate(seats):
            if s == 1:
                idx.append(i)
        res = -1
        res = max(res, idx[0])
        res = max(res, len(seats) -1 - idx[-1])
        for i in range(1, len(idx)):
            pre = idx[i-1]
            cur = idx[i]
            d = (cur - pre)/2
            res = max(res, d)
        return res