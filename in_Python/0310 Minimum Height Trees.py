class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if edges == None or len(edges) == 0:
            return [0]
        adj = {}
        for i in range(n):
            adj[i] = set()
        degree = [0] * n
        for e in edges:
            a = e[0]
            b = e[1]
            adj[a].add(b)
            adj[b].add(a)
            degree[a] += 1
            degree[b] += 1
        leaves = []
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
        while n > 2:
            L = len(leaves)
            while L != 0:
                L -= 1
                nex = leaves.pop(0)
                for x in adj[nex]:
                    degree[x] -= 1
                    if degree[x] == 1:
                        leaves.append(x)
                n -= 1
        return list(leaves)