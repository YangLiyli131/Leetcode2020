class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c1 = 0
        for i in range(len(s)):
            if s[i] == "A":
                c1 += 1
            if i < len(s)-2 and s[i:i+3] == "LLL":
                return False
        return c1 < 2