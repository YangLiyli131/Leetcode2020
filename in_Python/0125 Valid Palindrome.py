class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j = 0, len(s)-1
        while i < j:
            while not s[i].isalpha() and not s[i].isdigit() and i < j:
                i += 1
            while not s[j].isalpha() and not s[j].isdigit() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True