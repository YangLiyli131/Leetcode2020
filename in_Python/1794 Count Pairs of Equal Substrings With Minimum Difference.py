class Solution(object):
    def countQuadruples(self, firstString, secondString):
        """
        :type firstString: str
        :type secondString: str
        :rtype: int
        """
        base = 'abcdefghijklmnopqrstuvwxyz'
        d1 = {}
        d2 = {}
        for x in base:
            for i,t in enumerate(firstString):
                if t == x:
                    d1[x] = i
                    break
        for x in base:
            for i,t in enumerate(secondString):
                if t == x:
                    d2[x] = i
        r = 0
        df = sys.maxint
        for k in d1:
            if k in d2:
                d = d1[k] - d2[k]
                if d < df:
                    df = d
                    r = 1
                elif d == df:
                    r += 1
        return r