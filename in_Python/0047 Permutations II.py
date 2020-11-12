class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        visited = [False] * len(nums)
        
        def dfs(n, cur):
            if len(cur) == n:
                ans.append(cur[:])
                return 
            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                visited[i] = True
                cur.append(nums[i])
                dfs(n,cur)
                cur.pop()
                visited[i] = False
        dfs(len(nums),[])
        return ans
                