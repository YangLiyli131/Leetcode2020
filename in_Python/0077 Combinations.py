class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = list(range(1,n+1))
        def dfs(n, s, cur):
            if len(cur) == n:
                res.append(cur[:])
                return
            for i in range(s, len(nums)):
                cur.append(nums[i])
                dfs(n, i+1, cur)
                cur.pop()
        
        dfs(k, 0, [])
        return res