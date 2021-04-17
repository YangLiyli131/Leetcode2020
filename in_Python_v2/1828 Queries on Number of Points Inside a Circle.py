class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        for q in queries:
            xq, yq, r = q[0], q[1], q[2]
            n = 0
            for p in points:
                a,b = p[0], p[1]
                if (a - xq) * (a - xq) + (b - yq) * (b - yq) <= r * r:
                    n += 1
            res.append(n)
        return res