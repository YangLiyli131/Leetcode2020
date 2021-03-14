class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        i = 0
        r = []
        while i < len(s1):
            if s1[i] != s2[i]:
                r.append(i)
            i += 1
        if len(r) == 0:
            return True
        elif len(r) != 2:
            return False
        a,b = s1[r[0]],s1[r[1]]
        aa,bb = s2[r[0]],s2[r[1]]
        return a == bb and b == aa