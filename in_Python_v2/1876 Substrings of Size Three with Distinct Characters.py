class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        for i in range(3, len(s)+1):
            ss = s[i-3: i]
            x = set()
            for f in ss:
                x.add(f)
            if len(x) == 3:
                r += 1
        return r