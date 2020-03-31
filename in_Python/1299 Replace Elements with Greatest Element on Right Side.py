class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # scan from right to left
        if len(arr) == 1:
            return [-1]
        idx = len(arr)-1
        cur_max = arr[idx]
        while idx >= 0:
            temp = arr[idx-1]
            arr[idx-1] = cur_max
            if cur_max < temp: cur_max = temp
            idx -= 1
        arr[-1] = -1
        return arr