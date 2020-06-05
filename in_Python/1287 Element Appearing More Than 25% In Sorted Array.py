class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        L = len(arr)
        i = 0
        j = 0
        count = 0
        while j < len(arr):
            if arr[j] == arr[i]:
                count += 1
                j += 1
            else:
                if count > L/4:
                    return arr[i]
                else:
                    count = 0
                    i = j
        return arr[i]
        