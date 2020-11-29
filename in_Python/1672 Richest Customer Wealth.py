class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res = sum(accounts[0])
        for i in range(1, len(accounts)):
            cur = sum(accounts[i])
            res = max(res, cur)
        return res