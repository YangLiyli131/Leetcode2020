class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = {}
        p = 0
        while 2 ** p <= num:
            dp[2**p] = 1
            p += 1
        dp[0] = 0
        for i in range(3, num+1):
            if i in dp:
                continue
            pnear = 2 ** (int(log(i,2)))
            dp[i] = 1 + dp[i - pnear]
        res = []
        for k in range(num+1):
            res.append(dp[k])
        return res