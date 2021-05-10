class Solution(object):
    def distinctNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr = nums[0 : k]
        d = collections.Counter(arr)
        res = [len(d)]
        for i in range(k, len(nums)):
            rem = nums[i - k]
            come = nums[i]
            d[rem] -= 1
            if d[rem] == 0:
                d.pop(rem, None) 
            if come not in d:
                d[come] = 1
            else:
                d[come] += 1
            res.append(len(d))
        return res