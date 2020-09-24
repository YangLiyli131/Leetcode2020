class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        d = {}
        dis = []
        for i in range(R):
            for j in range(C):
                dx = abs(i-r0) + abs(j-c0)
                dis.append(dx)
                if dx not in d:
                    t = []
                    t.append([i,j])
                    d[dx] = t
                else:
                    t = d[dx]
                    t.append([i,j])
                    d[dx] = t
        dist = []
        for i in set(dis):
            dist.append(i)
        dist.sort()
        res = []
        for i in dist:
            cos = d[i]
            for x in cos:
                res.append(x)
        return res
        