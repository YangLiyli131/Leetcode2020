class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        cur = 0
        for i in range(len(s)):
            if s[i] == 'R':
                cur -= 1
            else:
                cur += 1
            if cur == 0:
                res += 1
        return res
        