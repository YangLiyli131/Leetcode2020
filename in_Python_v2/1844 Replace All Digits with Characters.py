class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dc = {}
        idx = 0
        ss = 'abcdefghijklmnopqrstuvwxyz'
        for x in ss:
            dc[x] = idx
            idx += 1
        r = []
        for i, x in enumerate(s):
            if i % 2 == 0:
                r.append(x)
            else:
                d = int(x)
                r.append(ss[dc[s[i-1]] + d])
                
        return ''.join(r)