class Solution(object):
    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]
    def overlaprange(self, a,b):
        return [max(a[0],b[0]), min(a[1],b[1])]
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i,j = 0,0
        res = []
        while i < len(A) and j < len(B):
            a = A[i]
            b = B[j]
            if a[1] < b[0]:
                i += 1
            elif b[1] < a[0]:
                j += 1
            elif self.overlap(a,b):
                over = self.overlaprange(a,b)
                res.append(over)
                if over[1] == b[1]:
                    j += 1
                if over[1] == a[1]:
                    i += 1
        return res
                
        