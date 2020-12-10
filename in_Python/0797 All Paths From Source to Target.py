class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0]]
        f = len(graph)-1
        added = True
        while added:
            cur = []
            added = False
            for x in res:
                last = x[-1]
                if last == f:
                    cur.append(x)
                    continue
                for y in graph[last]:
                    tmp = x + [y]
                    added = True
                    cur.append(tmp)
            res = cur
        return res
            