class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        d = 0
        for x in shift:
            if x[0] == 0:
                d -= x[1]
            else:
                d += x[1]
        d = d % len(s)
        if d == 0:
            return s
        elif d < 0:
            d = abs(d)
            news = s[d:] + s[0:d] 
        else:
            news = s[len(s)-d : ] + s[:len(s)-d]
        return news