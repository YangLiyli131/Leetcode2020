class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        if k == 0:
            return res
        i,j = 0,0
        d = {}
        n = len(s)
        while j < n:
            while j < n:
                cur = s[j]
                if len(d) < k:           
                    if cur not in d:
                        d[cur] = 1
                    else:
                        d[cur] += 1
                    j += 1
                else:
                    if cur in d:
                        d[cur] += 1
                        j += 1
                    else:
                        break
            res = max(res, j - i)
            while i < n and len(d) == k:
                pre = s[i]
                d[pre] -= 1
                if d[pre] == 0:
                    d.pop(pre, None)
                i += 1
        return res