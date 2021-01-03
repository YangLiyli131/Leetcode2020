class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        d = collections.Counter(A)
        bases = []
        keys = d.keys()
        n = len(keys)
        for i in range(n):
            a = keys[i]
            for j in range(n):
                b = keys[j]
                for k in range(n):
                    c = keys[k]
                    if i <= j <= k and a + b + c == target:
                        bases.append([a,b,c])
        
        for x in bases:
            a,b,c = x[0], x[1], x[2]
            dx = collections.Counter(x)
            if len(dx) == 3:
                res += d[a] * d[b] * d[c]
            elif len(dx) == 2:
                tmp = 1
                for dk in dx:
                    if dx[dk] == 2:
                        tmp *= d[dk] * (d[dk]-1) / 2
                    else:
                        tmp *= d[dk]
                res += tmp
            else:
                for dk in dx:
                    res += d[dk] * (d[dk]-1) * (d[dk]-2)/ 6
        return res % (1000000007)