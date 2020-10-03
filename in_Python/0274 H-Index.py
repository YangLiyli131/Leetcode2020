class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(citations)+1):
            d[i] = 0
        for c in citations:
            for x in range(c+1):
                if x in d:
                    d[x] += 1
        res = []
        for k in d:
            if k <= d[k]:
                res.append(k)
        res.sort()
        return res[-1]