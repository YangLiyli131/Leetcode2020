class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        L = len(nums)
        if k > len(nums):
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        ave = total / k
        buckets = [0] * k
        nums.sort(reverse = True)
    
        def dfs(i):
            if i == L:
                return True
            for j in range(k):
                buckets[j] += nums[i]
                if buckets[j] <= ave and dfs(i+1):
                    return True
                buckets[j] -= nums[i]
                if buckets[j] == 0:
                    break
            return False
        return dfs(0)
        
        
        