class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A == None or len(A) == 0:
            return 0
        total = 0
        res = 0
        idx = 0
        for i in A:
            total += i
            res += idx * i
            idx += 1
        N = len(A)
        result = res
        right = N-1
        for i in range(N-1):
            t = total - A[right]
            cur = res - A[right] * (N-1)
            res = cur + t
            result = max(result, res)
            right -= 1
        return result
        