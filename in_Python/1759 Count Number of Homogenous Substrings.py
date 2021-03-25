class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        r = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            l = j - i
            r += l * (l+1) / 2
            i = j
        return r % 1000000007
                