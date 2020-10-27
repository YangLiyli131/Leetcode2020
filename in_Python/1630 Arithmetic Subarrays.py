class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def check(arr):
            arr.sort()
            if len(arr) <= 2:
                return True
            d = arr[1] - arr[0]
            for i in range(2, len(arr)):
                dd = arr[i] - arr[i-1]
                if dd != d:
                    return False
            return True
        res = []
        for i in range(len(l)):
            a = l[i]
            b = r[i]
            res.append(check(nums[a:(b+1)]))
        return res
        