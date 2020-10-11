class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        res = 0
        for x in s:
            if x == '(':
                num += 1
                res = max(num,res)
            elif x == ')':
                num -= 1
        return res