class Solution(object):
    def window_sum(self, arr, w):
        r = 0
        i = 0
        j = i + w
        while j <= len(arr):
            t = i
            while t < j:
                r += arr[t]
                t += 1
            i += 1
            j = i + w
        return r
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        L = len(arr)
        i = 1
        res = 0
        while i <= L:
            res += self.window_sum(arr,i)
            i += 2
        return res