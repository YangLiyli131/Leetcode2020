class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for si in s:
            if si not in d:
                d[si] = 1
            else:
                d[si] += 1
        res = ''
        for ti in t:
            if ti not in d:
                return ti
            else:
                d[ti] -= 1
                if d[ti] < 0:
                    res = ti
                    break
        return res