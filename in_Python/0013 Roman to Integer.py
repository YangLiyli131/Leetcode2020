class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        d["I"] = 1
        d["V"] = 5
        d["X"] = 10
        d["L"] = 50
        d["C"] = 100
        d["D"] = 500
        d["M"] = 1000
        d["IV"] = 4
        d["IX"] = 9
        d["XL"] = 40
        d["XC"] = 90
        d["CD"] = 400
        d["CM"] = 900
        res = 0
        i = 0
        while i < len(s)-1:
            s1 = s[i]
            s2 = s[i:i+2]
            if s2 in d:
                res += d[s2]
                i += 2
            else:
                res += d[s1]
                i += 1
        if i < len(s):
            res += d[s[i]]
        return res