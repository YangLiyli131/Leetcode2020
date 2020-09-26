class Solution(object):
    def hep(self, M, i, j):
        s = 0
        c = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if (x >= 0 and x < len(M)) and (y >= 0 and y < len(M[0])):
                    s += M[x][y]
                    c += 1
        return s / c
        
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(M)):
            cur = []
            for j in range(len(M[0])):
                cur.append(self.hep(M, i, j))
            res.append(cur)
        return res