class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        i,j = 0,0
        res = 0
        d = {}
        for i in range(N):
            c = s[i]
            if c not in d or d[c] == -1:
                d[c] = i
                res = max(res, i - j + 1)
            else:
                res = max(res, i - j)
                j = d[c] + 1
                m = d[c]
                for k in d:
                    if d[k] <= m:
                        d[k] = -1     
                d[c] = i
        return res