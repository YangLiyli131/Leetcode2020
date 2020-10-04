class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        mat = []
        for i in range(N):
            c = []
            for j in range(N):
                c.append(0)
            mat.append(c)
        for i in range(N):
            cur = points[i]
            for j in range(i+1, N):
                node = points[j]
                d = (cur[0] - node[0]) * (cur[0] - node[0]) + (cur[1] - node[1]) * (cur[1] - node[1])
                mat[i][j] = d
                mat[j][i] = d
        res = 0
        for i in range(N):
            row = mat[i]
            d = {}
            for r in row:
                if r == 0:
                    continue
                if r not in d:
                    d[r] = 1
                else:
                    d[r] += 1
            for k in d:
                u = d[k]
                res += u * (u-1)
        return res
                    