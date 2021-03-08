class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        d = {}
        d[1] = ['0','1','8']
        d[2] = ['11','69','88','96']
        if n <= 2:
            return d[n]
        i = 3
        while i <= n:
            pre = d[i-2]
            c = ['0'] * (i-2)
            cc = ''.join(c)
            pre.append(cc)
            cur = []
            for x in pre:
                cur.append('1' + x + '1')
                cur.append('8' + x + '8')
                cur.append('6' + x + '9')
                cur.append('9' + x + '6')
                cur.append('0' + x + '0')
            d[i] = cur
            i += 1
        r = []
        base = set()
        for x in d[n]:
            if x[0] != '0' and x not in base:
                r.append(x)
                base.add(x)
        return r