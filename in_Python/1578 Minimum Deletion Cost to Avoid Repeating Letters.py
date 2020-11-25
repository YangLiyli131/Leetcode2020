class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        res = 0
        i,j = 0,0
        
        while j < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            r = list(range(i,j))
            if len(r) == 1:
                i = j
                continue
            cur = cost[i:j]
            res += sum(cur) - max(cur)
            i = j
        return res
            
        