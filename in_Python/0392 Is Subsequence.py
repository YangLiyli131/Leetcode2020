class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i,j = 0,0
        while j < len(t):
            if i == len(s):
                return True
            if t[j] == s[i]:
                i += 1
            j += 1
        return i == len(s)
        