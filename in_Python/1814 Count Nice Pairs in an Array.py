class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rev = {}
        for x in nums:
            if x in rev:
                continue
            xx = x
            cur = 0
            while x != 0:
                cur = cur * 10 + x % 10
                x /= 10
            rev[xx] = cur
        res = 0
        twosummap = {}
        for i in range(len(nums)):
            val = nums[i]
            revval = rev[val]
            dif = val - revval
            if dif not in twosummap:
                twosummap[dif] = []
            twosummap[dif].append(i)
        for k in twosummap:
            v = len(twosummap[k]) - 1
            res += (v + 1) * v / 2
        return res % 1000000007
            
            