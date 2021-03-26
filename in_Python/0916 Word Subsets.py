class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        r = []
        
        bmax = {}
        for s in 'abcdefghijklmnopqrstuvwxyz':
            bmax[s] = 0
        for b in B:
            db = collections.Counter(b)
            for k in db:
                bmax[k] = max(bmax[k], db[k])  
        for a in A:
            d = collections.Counter(a)
            f = 1
            for k in d:
                if d[k] < bmax[k]:
                    f = 0
                    break
            for k in bmax:
                if bmax[k] != 0 and k not in d:
                    f = 0
                    break
            if f == 1:
                r.append(a)
        return r
                