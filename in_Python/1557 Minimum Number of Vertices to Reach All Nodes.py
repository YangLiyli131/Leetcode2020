class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        in_d = [0] * n
        for e in edges:
            t = e[1]
            in_d[t] += 1
        res = []
        for x in range(n):
            if in_d[x] == 0:
                res.append(x)
        return res
        