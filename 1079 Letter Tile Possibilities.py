class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        d = collections.Counter(tiles)
        base = set()
        for x in tiles:
            base.add(x)
        res = len(base)
        bt = []
        for x in base:
            dd = d.copy()
            dd[x] -= 1
            bt.append([x, dd])
        f = True
        while f:
            f = False
            cur = []
            for x in bt:
                pre = x[0]
                pd = x[1]
                for k in pd:
                    if pd[k] != 0:
                        pp = pre + k
                        pdd = pd.copy()
                        pdd[k] -= 1
                        f = True
                        res += 1
                        cur.append([pp, pdd])
            bt = cur
        return res
                        
        
        