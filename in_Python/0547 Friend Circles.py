class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = []
        res = 0
        for i in range(len(M)):
            if i in visited:
                continue
            q = []
            q.append(i)
            visited.append(i)
            while len(q) != 0:
                n = len(q)
                for p in range(n):
                    head = q.pop(0)
                    L = M[head]
                    for idx in range(len(L)):
                        if L[idx] == 1:
                            if idx not in visited:
                                visited.append(idx)
                                q.append(idx)
            res += 1            
        return res
                    