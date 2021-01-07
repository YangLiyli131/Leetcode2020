class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        A = {}
        for e in edges:
            a = e[0]
            b = e[1]
            if a not in A:
                A[a] = [b]
            else:
                A[a].append(b)
            if b not in A:
                A[b] = [a]
            else:
                A[b].append(a)
                
        k = A.keys()[0]
        q = collections.deque()
        q.append(k)
        length = -1
        seen = set()
        seen.add(k)
        last = None
        while q:
            n = len(q)
            length += 1
            while n != 0:
                n -= 1
                h = q.popleft()
                for nex in A[h]:
                    if nex not in seen:
                        seen.add(nex)
                        q.append(nex)
                last = h
        
        q = collections.deque()
        q.append(last)
        length = -1
        seen = set()
        seen.add(last)
        while q:
            n = len(q)
            length += 1
            while n != 0:
                n -= 1
                h = q.popleft()
                for nex in A[h]:
                    if nex not in seen:
                        seen.add(nex)
                        q.append(nex)
        return length
        
                    