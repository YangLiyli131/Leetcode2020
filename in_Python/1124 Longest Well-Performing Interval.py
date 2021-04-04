class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        arr = []
        for x in hours:
            if x > 8:
                arr.append(1)
            else:
                arr.append(-1)
        cs = [0]
        for x in arr:
            cs.append(x + cs[-1])
        d = {}
        for i,x in enumerate(cs):
            if x not in d:
                d[x] = []
            d[x].append(i)
        res = 0
        for j in d:
            rj = d[j]
            for i in d:
                if i < j:
                    ri = d[i]
                    dis = rj[-1] - ri[0]
                    res = max(res, dis)
        return res