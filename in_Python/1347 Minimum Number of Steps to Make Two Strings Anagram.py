class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        res = 0
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 not in d1:
                d1[c1] = 1
            else:
                d1[c1] += 1
            if c2 not in d2:
                d2[c2] = 1
            else:
                d2[c2] += 1
        for c in d2:
            if c in d1 and d2[c] > d1[c]:
                res += d2[c] - d1[c]
            if c not in d1:
                res += d2[c]
        return res