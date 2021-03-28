class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = list(range(n))
        b = arr[:]
        r = 0
        arr2 = [0] * n
        while arr2 != b:
            for i in range(n):
                if i % 2 == 0:
                    arr2[i] = arr[i / 2]
                else:
                    arr2[i] = arr[n / 2 + (i-1) / 2]
            r += 1
            arr = arr2[:]
        return r
