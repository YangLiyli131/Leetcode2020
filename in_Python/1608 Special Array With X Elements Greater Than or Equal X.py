class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for i in range(len(nums)+1):
            arr.append(0)
        for i in nums:
            for j in range(i+1):
                if j < len(arr):
                    arr[j] += 1
        for i in range(len(arr)):
            if i == arr[i]:
                return i
        return -1
        