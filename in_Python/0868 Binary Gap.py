class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        idx = 0
        last = 0
        while N % 2 != 1:
            N /= 2
            last += 1
            idx += 1
        N /= 2
        #print(last)
        idx += 1
        while N != 0:
            if N % 2 == 1:
                cur = idx
                res = max(res, cur - last)
                last = cur
            idx += 1
            N /= 2
        #print(last)
        #print(cur)
        return res