class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [-1] * n
        for i in range(n):
            if color[i] != -1:
                continue
            color[i] = 1
            q = [i]
            while q:
                h = q.pop(0)
                for j in graph[h]:
                    if color[j] == -1:
                        color[j] = 1 - color[h]
                        q.append(j)
                    elif color[j] == color[h]:
                        return False
        return True