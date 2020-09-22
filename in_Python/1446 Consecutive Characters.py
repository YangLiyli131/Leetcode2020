class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        i = 0
        j = i
        p = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            p = max(p, j-i)
            i = j
        return p