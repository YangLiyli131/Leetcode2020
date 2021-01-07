class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        visited = set()
        q = collections.deque()
        q.append(s)
        res = s
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.popleft()
                added = []
                for i in range(len(h)):
                    if i % 2 == 0:
                        added.append(h[i])
                    else:
                        it = int(h[i])
                        it += a
                        if it >= 10:
                            it -= 10
                        added.append(str(it))
                added = ''.join(added)
                if added not in visited:
                    visited.add(added)
                    q.append(added)
                
                rotated = h[b:] + h[:b] 
                if rotated not in visited:
                    visited.add(rotated)
                    q.append(rotated)
                
                res = min(res, h)
        return res