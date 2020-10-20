class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n-1:
            return -1
        d = {}
        for i in range(n):
            d[i] = []
        for c in connections:
            a = c[0]
            b = c[1]
            d[a].append(b)
            d[b].append(a)
        visited = [0] * n
        res = 0
        
        def dfs(i):
            if visited[i] == 1:
                return 0
            visited[i] = 1
            for j in d[i]:
                dfs(j)
            return 1
        
        for i in range(n):
            res += dfs(i)
        return res-1