class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(2, len(arr)):
            dd = arr[i] - arr[i-1]
            if dd != d:
                return False
        return True