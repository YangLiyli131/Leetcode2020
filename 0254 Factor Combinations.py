class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        base = set()
        for i in range(2, n/2 + 1):
            if n % i == 0:
                cur = sorted([i, n / i])
                base.add(tuple(cur))
        if not base:
            return base
        res = base.copy()
        f = 1
        while f == 1:
            f = 0
            cur = set()
            for pre in base:
                num = pre[-1]
                for i in range(2, num/2+1):
                    if num % i == 0:
                        cur.add(tuple(sorted(list(pre[:-1]) + [i, num/i])))
                        res.add(tuple(sorted(list(pre[:-1]) + [i, num/i])))
                        f = 1
            base = cur.copy()
        return res
            
        