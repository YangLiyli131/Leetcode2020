class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        i,j = 0,0
        ca,cb,cc = 0,0,0
        res = 0
        while i < N:
            if s[i] == 'a':
                ca += 1
            elif s[i] == 'b':
                cb += 1
            else:
                cc += 1
            while ca >= 1 and cb >= 1 and cc >= 1 and j < N:
                res += N - i
                if s[j] == 'a':
                    ca -= 1
                elif s[j] == 'b':
                    cb -= 1
                else:
                    cc -= 1
                j += 1
            i += 1
        return res