class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        la = sorted(s)
        lb = sorted(t)
        for i in range(len(s)):
            if la[i] != lb[i]:
                return False
        return True
        
        