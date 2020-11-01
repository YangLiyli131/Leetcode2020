class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = len(candidates)
        res = []
        
        def dfs(s, e, num, cur):
            if num == 0:
                res.append(cur[:])
            if num < 0:
                return
            for i in range(s,e):
                cur.append(candidates[i])
                dfs(i,e, num - candidates[i], cur)
                cur.pop()
        
        dfs(0, N, target, [])
        return res