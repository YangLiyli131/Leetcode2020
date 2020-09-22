class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        i = 0
        while i+2 < len(arr):
            a = arr[i]
            b = arr[i+1]
            c = arr[i+2]
            if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
                return True
            i += 1
        return False