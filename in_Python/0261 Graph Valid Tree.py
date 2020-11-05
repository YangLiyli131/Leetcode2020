class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if edges == None or len(edges) == 0:
            if n == 1:
                return True
            else:
                return False
    
        degree = [0] * n
        adj = {}
        for i in range(n):
            adj[i] = []
        for e in edges:
            a = e[0]
            b = e[1]
            degree[a] += 1
            degree[b] += 1
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [0] * n
        q = [0]
        while q:
            h = q.pop(0)
            visited[h] = 1
            for x in adj[h]:
                if visited[x] != 1:
                    q.append(x)
        if sum(visited) != n:
            return False         
            
        q = []
        for i in range(n):
            if degree[i] == 0:
                return False
            if degree[i] == 1:
                q.append(i)
        for x in q:
            for y in adj[x]:
                degree[y] -= 1
                if degree[y] == 1:
                    q.append(y)
        return len(q) == n