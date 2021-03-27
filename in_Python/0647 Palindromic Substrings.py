class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = set()
        for x in s:
            p.add(x)
        n = len(s)
        r = n
        j = 2
        while j <= n:
            cs = s[j-2:j]
            if cs[0] == cs[-1]:
                p.add(cs)
                r += 1
            j += 1
        l = 3
        while l <= n:
            j = l
            while j <= n:
                cs = s[j-l : j]
                if cs[0] == cs[-1] and cs[1:-1] in p:
                    p.add(cs)
                    r += 1
                j += 1
            l += 1
        return r
                