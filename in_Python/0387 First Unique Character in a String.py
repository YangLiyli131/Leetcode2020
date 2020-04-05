class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for i in range(len(s)):
            c = s[i]
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
        if 1 not in dict.values(): return -1
        
        res = len(s)+1
        for k in dict:
            if dict[k] == 1:
                v = s.index(k)
                if v < res:
                    res = v
        return res
                