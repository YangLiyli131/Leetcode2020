class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = []
        maxnum = 0
        minnum = 0
        x = ''
        y = ''
        if A >= B:
            maxnum = A
            minnum = B
            x = 'a'
            y = 'b'
        else:
            maxnum = B
            minnum = A
            x = 'b'
            y = 'a'
        while minnum != 0:
            res.append(x)
            res.append(y)
            minnum -= 1
            maxnum -= 1
        if maxnum != 0:
            res.append(x)
            maxnum -= 1
        idx = 0
        while maxnum != 0:
            res[idx] += x
            maxnum -= 1
            idx += 2
        return ''.join(res)
        
        
        