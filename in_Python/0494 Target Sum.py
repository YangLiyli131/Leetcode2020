class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        idx = len(nums)-1
        cursum = 0
        self.memo = {}
        return self.dp(nums, S, idx, cursum)
    def dp(self, n, target, idx, cursum):
        if (idx, cursum) in self.memo:
            return self.memo[(idx, cursum)]
        if idx < 0 and cursum == target:
            return 1
        if idx < 0:
            return 0
        pos = self.dp(n, target, idx-1, cursum + n[idx])
        neg = self.dp(n, target, idx-1, cursum - n[idx])
        self.memo[(idx, cursum)] = pos + neg
        return pos + neg

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        d = {0:1}
        for x in nums:
            steps = collections.Counter()
            for k in d:
                steps[k+x] += d[k]
                steps[k-x] += d[k]
            d = steps
        return d[S]