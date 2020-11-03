class Solution(object):
    def check(self, s):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return self.check(s[0:i] + s[(i+1):]) or self.check(s[0:j] + s[(j+1):])
            i += 1
            j -= 1
        return True