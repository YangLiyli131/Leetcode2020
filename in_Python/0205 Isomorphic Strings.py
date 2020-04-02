class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        dict = {}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if a not in dict and b not in dict.values():
                dict[a] = b
            if a in dict and dict[a] != b:
                return False
            if a not in dict and b in dict.values():
                return False
        return True