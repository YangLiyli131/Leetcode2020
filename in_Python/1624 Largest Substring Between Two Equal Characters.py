class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        res = -1
        for i in range(len(s)):
            cur = s[i]
            if cur not in d:
                d[cur] = i
            else:
                r = i - d[cur] - 1
                res = max(res, r)
        return res