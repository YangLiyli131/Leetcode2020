class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        # scan from right to left
        res = ""
        i = len(s)-1
        while i >= 0:
            if s[i] == '#':
                res = chr(ord('a') + int(s[(i-2):i]) - 1) + res
                i -= 3
            else:
                res = chr(ord('a') + int(s[i]) - 1) + res
                i -= 1
        return res
            