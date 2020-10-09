class Solution(object):
    def isV(self, c):
        if c in ['a','e','i','o','u']:
            return True
        return False
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        counter = 0
        for i in range(len(s)):
            if self.isV(s[i]):
                counter += 1
            if i >= k:
                if self.isV(s[i-k]):
                    counter -= 1
            res = max(res, counter)
        return res