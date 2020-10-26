class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == None:
            return []
        N = len(nums)
        if N == 1:
            return [str(nums[0])]
        temp = []
        i = 0
        j = 1
        while j < N:
            j = i + 1
            while j < N and nums[j] == nums[j-1]+1:               
                j += 1
            cur = [nums[i], nums[j-1]]
            temp.append(cur)
            i = j
        res = []
        for x in temp:
            a = x[0]
            b = x[1]
            if a == b:
                res.append(str(a))
            else:
                res.append(str(a) + '->' + str(b))
        return res