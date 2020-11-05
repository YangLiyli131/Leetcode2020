class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = version1.split('.')
        A = []
        for x in l1:
            xs = list(x)
            cur = 0
            while xs:
                left = int(xs.pop(0))
                cur = cur * 10 + left
            A.append(cur)
        l2 = version2.split('.')
        B = []
        for x in l2:
            xs = list(x)
            cur = 0
            while xs:
                left = int(xs.pop(0))
                cur = cur * 10 + left
            B.append(cur)
        LA = len(A)
        LB = len(B)
        d = LA - LB
        while d > 0:
            B.append(0)
            d -= 1
        while d < 0:
            A.append(0)
            d += 1
        i = 0
        while i < len(A):
            if A[i] < B[i]:
                return -1
            elif A[i] > B[i]:
                return 1
            else:
                i += 1
        return 0