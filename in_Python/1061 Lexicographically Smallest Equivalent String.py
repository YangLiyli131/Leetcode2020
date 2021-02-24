class Solution(object):
    def smallestEquivalentString(self, A, B, S):
        """
        :type A: str
        :type B: str
        :type S: str
        :rtype: str
        """
        n = len(A)
        d = {}
        for i in range(n):
            a,b = A[i], B[i]
            if a not in d:
                d[a] = [b]
            else:
                if b not in d[a]:
                    d[a].append(b)
            if b not in d:
                d[b] = [a]
            else:
                if a not in d[b]:
                    d[b].append(a)
        r = []
        for i in range(len(S)):
            cur = S[i]
            seen = set()
            seen.add(cur)
            q = collections.deque()
            q.append(S[i])
            while q:
                h = q.popleft()
                cur = min(cur, h)
                if h in d:                    
                    for x in d[h]:
                        if x not in seen:
                            seen.add(x)
                            q.append(x)
            r.append(cur)
        return ''.join(r)
        