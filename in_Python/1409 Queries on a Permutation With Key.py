class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        d = {}
        res = []
        for i in range(1,m+1):
            d[i] = i-1
        for q in queries:
            res.append(d[q])
            for k in d:
                if d[k] < d[q]:
                    d[k] += 1
            d[q] = 0
        return res
        