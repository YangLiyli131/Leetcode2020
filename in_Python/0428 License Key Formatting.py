class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        count = 0
        for i in range(len(S)-1, -1, -1):
            x = S[i]
            if x == '-':
                continue
            if '0' <= x <= '9':
                res.insert(0,x)
            elif 'A' <= x <= 'Z':
                res.insert(0,x)
            elif 'a' <= x <= 'z':
                x = x.upper()
                res.insert(0,x)
            count += 1
            if count == K:
                res.insert(0,'-')
                count = 0        
        if res and res[0] == '-':
            res = res[1:]
        return ''.join(res)