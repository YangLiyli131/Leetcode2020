class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        dc = []
        lc = []
        for si in s:
            if si.isdigit():
                dc.append(si)
            else:
                lc.append(si)
        if abs(len(dc) - len(lc)) > 1:
            return ""
        res = ''
        if len(dc) > len(lc):
            for i in range(len(lc)):
                res += dc[i]
                res += lc[i]
            res += dc[-1]
        elif len(dc) < len(lc):
            for i in range(len(dc)):
                res += lc[i]
                res += dc[i]
            res += lc[-1]
        else:
            for i in range(len(dc)):
                res += lc[i]
                res += dc[i]
        return res