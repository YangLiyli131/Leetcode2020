class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = collections.Counter(list(s))
        odd = 0
        for k in d:
            if d[k] % 2 == 1:
                odd += 1
                if odd > 1: 
                    return False
        return True