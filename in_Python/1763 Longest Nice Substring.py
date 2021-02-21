class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        r, l = '', 0
        
        def check(s):
            m = 'abcdefghijklmnopqrstuvwxyz'
            n = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for i in range(len(m)):
                a,b = m[i], n[i]
                if (a not in s and b in s) or (a in s and b not in s):
                    return False
            return True
        
        for i in range(len(s)-1):
            for j in range(i+1, len(s)+1):
                cs = s[i:j]
                if check(cs) and len(cs) > l:
                    r = cs
                    l = len(cs)
        return r