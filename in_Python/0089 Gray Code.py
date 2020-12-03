class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        up = pow(2,n) - 1
        L = ['0' * n]
        d = set()
        d.add('0' * n)
        while up != 0:
            up -= 1
            pre = L[-1]
            for i in range(n):
                left = pre[:i]
                right = pre[i+1:]
                cur = pre[i]
                newcur = '1'
                if cur == '1':
                    newcur = '0'
                ns = left + newcur + right
                if ns not in d:
                    d.add(ns)
                    L.append(ns)
                    break
        for x in L[1:]:
            cur = 0
            for j in range(n-1,-1,-1):
                ch = x[j]
                it = int(ch)
                cur += it * pow(2, n-1-j)
            res.append(cur)
        return res