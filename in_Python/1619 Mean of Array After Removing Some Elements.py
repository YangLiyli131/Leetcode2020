class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        N = len(arr)
        arr.sort()
        total = 0
        for i in arr:
            total += i
        k = int(floor(N * 5 / 100))
        kk = k
        i = 0
        j = len(arr)-1
        while k != 0:
            k -= 1
            total -= arr[i]
            total -= arr[j]
            i += 1
            j -= 1
        return total / float(N - kk - kk)
        