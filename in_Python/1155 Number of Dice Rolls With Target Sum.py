class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        memo = {}
        
        def dp(n, t):
            if n == 0:
                return 0 if t > 0 else 1
            if (n,t) in memo:
                return memo[(n,t)]
            res = 0
            for i in range(max(0, t - f), t):
                res += dp(n-1, i)
            memo[(n,t)] = res
            return res
        
        return dp(d, target) % 1000000007