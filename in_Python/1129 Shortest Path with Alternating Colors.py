class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        d = {}
        for r in red_edges:
            s = r[0]
            e = r[1]
            if s not in d:
                d[s] = [[e,'r']]
            else:
                d[s].append([e,'r'])
        for b in blue_edges:
            s = b[0]
            e = b[1]
            if s not in d:
                d[s] = [[e,'b']]
            else:
                d[s].append([e,'b'])
        res = [-1] * n
        res[0] = 0
        level = 0
        q = collections.deque()
        q.append([0,''])
        seen = set()
        seen.add((0,''))
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                node, color = q.popleft()
                if node in d:
                    for nex in d[node]:
                        if tuple(nex) in seen:
                            continue
                        if nex[1] != color:
                            seen.add(tuple(nex))
                            q.append(nex)
                if res[node] == -1:
                    res[node] = level
                else:
                    res[node] = min(res[node], level)
            level += 1
        return res