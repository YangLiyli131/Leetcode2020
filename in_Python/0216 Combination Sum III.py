class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        nums = list(range(9, 0, -1))
        
        def dfs(s,e,num, target, cur):
            if target == 0 and num == 0:
                res.append(cur[:])
                return
            for i in range(s,e):
                cur.append(nums[i])
                dfs(i+1, e, num-1, target - nums[i], cur)
                cur.pop()
        
        dfs(0, 9, k, n, [])
        return res