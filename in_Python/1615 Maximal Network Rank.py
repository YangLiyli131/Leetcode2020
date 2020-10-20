class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = []
        for i in range(n):
            row = [0] * n
            graph.append(row)
        degree = [0] * n
        for r in roads:
            a = r[0]
            b = r[1]
            degree[a] += 1
            degree[b] += 1
            graph[a][b] = 1
            graph[b][a] = 1
        res = -1
        for i in range(n):
            for j in range(i+1,n):
                cur = degree[i] + degree[j] - graph[i][j]
                res = max(res,cur)
        return res