class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        logs = sorted(logs, key = lambda x : x[0])
        comp = collections.deque()
        for x in range(N):
            comp.append([x])
            
        def merge(a, b):
            r = set()
            for x in a:
                r.add(x)
            for x in b:
                r.add(x)
            return list(r)
            
        for x in logs:
            t,a,b = x[0],x[1],x[2]
            nfa, nfb = True, True
            aplace, bplace = None, None
            while nfa or nfb:
                cur = comp.popleft()
                if a in cur and b in cur:
                    aplace = cur
                    bplace = cur
                    nfa = False
                    nfb = False
                elif a in cur:
                    aplace = cur
                    nfa = False
                elif b in cur:
                    bplace = cur
                    nfb = False
                else:
                    comp.append(cur)
            newplace = merge(aplace, bplace)
            if len(newplace) == N:
                return t
            comp.append(newplace)

        return -1