class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        c = {}
        left = None
        for x in adjacentPairs:
            a = x[0]
            b = x[1]
            if a not in c:
                c[a] = [b]
            else:
                c[a].append(b)
            if b not in c:
                c[b] = [a]
            else:
                c[b].append(a)
            
        for k in c:
            if len(c[k]) == 1:
                left = k
                break
        res = []
        v = set()
        v.add(left)
        q = collections.deque()
        q.append(left)
        while q:
            h = q.popleft()
            res.append(h)
            for nex in c[h]:
                if nex not in v:
                    v.add(nex)
                    q.append(nex)
        return res
        