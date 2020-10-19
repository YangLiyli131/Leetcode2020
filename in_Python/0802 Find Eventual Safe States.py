class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        def dfs(i):
            visited[i] = 0
            for ii in graph[i]:
                if visited[ii] == 0 or (visited[ii] == -1 and dfs(ii)):
                    return True
            res.append(i)
            visited[i] = 1
            return False
        
        visited = [-1] * len(graph)
        res = []
        for i in range(len(graph)):
            if visited[i] == -1:
                dfs(i)
        res.sort()
        return res