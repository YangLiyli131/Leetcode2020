class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        visited = [False] * len(nums)
        
        def dfs(n, cur):
            if len(cur) == n:
                ans.append(cur[:])
                return 
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                cur.append(nums[i])
                dfs(n,cur)
                cur.pop()
                visited[i] = False
        dfs(len(nums),[])
        return ans