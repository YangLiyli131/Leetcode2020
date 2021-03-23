class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        def fac(x):
            return x * (x+1) // 2
        if '1' not in s:
            return 0
        if '0' not in s:
            return fac(len(s)) % 100000007
        x = s.split('0')
        r = 0
        for xx in x:
            r += fac(len(xx)) 
        return r % 1000000007