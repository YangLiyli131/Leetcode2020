class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j = 0, len(s)-1
        v = ['a','e','i','o','u','A','E','I','O','U']
        left, right = 0,0
        while i < j:
            a = s[i]
            b = s[j]
            if a in v:
                left += 1
            if b in v:
                right += 1
            i += 1
            j -= 1
        return left == right