class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        N = len(candidates)
        
        def dfs(s,e,num,cur):
            if num == 0:
                res.append(cur[:])
            elif num > 0:
                for i in range(s,e):
                    if i > s and candidates[i] == candidates[i-1]:
                        continue
                    cur.append(candidates[i])
                    dfs(i+1, e, num - candidates[i], cur)
                    cur.pop()
        candidates.sort(reverse = True)
        dfs(0, N, target, [])
        return res