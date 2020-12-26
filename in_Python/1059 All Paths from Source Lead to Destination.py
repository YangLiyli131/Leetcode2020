class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        g = collections.defaultdict(set)
        v = collections.defaultdict(int)
        for u,k in edges:
            g[u].add(k)
        
        def dfs(node):
            if v[node] == 1:
                return True
            elif v[node] == -1:
                return False
            elif len(g[node]) == 0:
                return node == destination
            else:
                v[node] = -1
                for ch in g[node]:
                    if not dfs(ch):
                        return False
                v[node] = 1
                return True
        return dfs(source)