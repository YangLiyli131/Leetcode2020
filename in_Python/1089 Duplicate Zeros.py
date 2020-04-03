class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        dict = {}
        num_zero = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                num_zero += 1
            else:
                dict[i + num_zero] = arr[i]
        
        for idx in range(len(arr)):
            if idx in dict:
                arr[idx] = dict[idx]
            else:
                arr[idx] = 0
        
        