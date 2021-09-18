class Solution(object):
    def isDecomposable(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        t = False
        while i < len(s):
            if i < len(s) - 2 and s[i] == s[i+1] == s[i+2]:
                i += 3
            elif i < len(s) - 1 and s[i] == s[i+1] and not t:
                t = True
                i += 2
            else:
                return False
        return t