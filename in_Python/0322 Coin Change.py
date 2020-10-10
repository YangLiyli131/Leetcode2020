class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] * (amount+1)
        for i in range(1, amount+1):
            cur = -1
            for c in coins:
                if i - c == 0:
                    cur = 1
                    break
                elif i - c > 0:
                    if dp[i-c] <= 0:
                        continue
                    if cur == -1:
                        cur = dp[i-c] + 1
                    else:
                        cur = min(cur, dp[i-c]+1)
            dp[i] = cur
        #print(dp)
        return dp[-1]