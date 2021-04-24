class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = collections.defaultdict(list)
        self.num = 0
        for x in connections:
            graph[x[0]].append(x[1])
            graph[x[1]].append(x[0])
        dfs_num, dfs_low = [None] * n, [None] * n
        def dfs(node, par):
            if dfs_num[node] is not None:
                return
            dfs_num[node] = dfs_low[node] = self.num
            self.num += 1
            for nex in graph[node]:
                if not dfs_num[nex]:
                    dfs(nex, node)
            dfs_low[node] = min([dfs_num[node]] + [dfs_low[nex] for nex in graph[node] if nex != par])
             
        dfs(0, None)

        res = []
        for u,v in connections:
            if dfs_low[u] > dfs_num[v] or dfs_low[v] > dfs_num[u]:
                res.append([u,v])
        return res
        