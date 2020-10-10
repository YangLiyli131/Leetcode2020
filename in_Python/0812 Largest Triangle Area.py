class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = -1
        N = len(points)
        for i in range(N):
            a = points[i]
            for j in range(i+1,N):
                b = points[j]
                for k in range(j+1, N):
                    c = points[k]
                    d_ab = (b[1] - a[1]) * (b[1] - a[1]) + (b[0] - a[0]) * (b[0] - a[0])
                    d_ac = (c[1] - a[1]) * (c[1] - a[1]) + (c[0] - a[0]) * (c[0] - a[0])
                    d_cb = (b[1] - c[1]) * (b[1] - c[1]) + (b[0] - c[0]) * (b[0] - c[0])
                    L = [d_ab, d_ac, d_cb]
                    L.sort()
                    if sqrt(L[0]) + sqrt(L[1]) > sqrt(L[2]):
                        area = ((b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])) / float(2)
                        res = max(res, abs(area))
        return res