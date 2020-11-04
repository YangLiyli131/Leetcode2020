class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = [0] * n
        adj = {}
        res = 0
        for i in range(n):
            adj[i] = []
        for e in edges:
            a = e[0]
            b = e[1]
            adj[a].append(b)
            adj[b].append(a)
        for i in range(n):
            if visited[i] == 1:
                continue
            visited[i] = 1
            res += 1
            q = adj[i]
            while q:
                x = q.pop(0)
                if visited[x] == 0:
                    visited[x] = 1
                    for nex in adj[x]:
                        if visited[nex] == 0:
                            q.append(nex)
        return res