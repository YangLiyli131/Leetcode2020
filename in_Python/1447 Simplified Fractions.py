class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        d = {}
        for x in range(1,n+1):
            cur = set()
            cur.add(1)
            cur.add(x)
            for i in range(1, x/2+1):
                if x % i == 0:
                    cur.add(i)
            d[x] = cur
        r = []
        for x in range(1, n+1):
            for y in range(1, x):
                t = d[x].intersection(d[y])
                if len(t) == 1 and t.pop() == 1:
                    r.append(str(y) + '/' + str(x))
        return r