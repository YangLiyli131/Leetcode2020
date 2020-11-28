class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return [max(nums)]
        if k == 1:
            return nums
        q = collections.deque()
        j = k-1
        for i in range(k):
            q.append(nums[i])
        i = 0
        res = [max(q)]
        j += 1
        while j < len(nums):
            premax = res[-1]
            left = q.popleft()
            right = nums[j]
            q.append(right)
            if left == premax or right > premax:
                res.append(max(q))
            else:
                res.append(premax)
            j += 1
        return res