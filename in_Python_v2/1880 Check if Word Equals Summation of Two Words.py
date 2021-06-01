class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        d = {}
        for i, x in enumerate('abcdefghijklmnopqrstuvwxyz'):
            d[x] = i
        def helper(s):
            r = 0
            for x in s:
                r = r * 10 + d[x]
            return r
        return helper(firstWord) + helper(secondWord) == helper(targetWord)
        