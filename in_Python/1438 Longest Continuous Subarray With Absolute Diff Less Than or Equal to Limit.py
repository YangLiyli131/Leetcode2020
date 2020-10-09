class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        maxd, mind = deque(), deque()
        i, j = 0, 0
        res = 0
        while j < len(nums):
            while maxd and nums[j] >= nums[maxd[-1]]:
                maxd.pop()
            while mind and nums[j] <= nums[mind[-1]]:
                mind.pop()
            maxd.append(j)
            mind.append(j)
            while nums[maxd[0]] - nums[mind[0]] > limit:
                i += 1
                if i > maxd[0]:
                    maxd.popleft()
                if i > mind[0]:
                    mind.popleft()
            res = max(res, j - i + 1)
            j += 1
        return res