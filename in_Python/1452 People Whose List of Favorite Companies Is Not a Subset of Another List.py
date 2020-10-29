class Solution(object):
    def check(self, a, b):
        xb = set(b)
        for ai in a:
            if ai not in xb:
                return False
        return True
        
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        d = {}
        idx = 0
        for coms in favoriteCompanies:
            for com in coms:
                if com not in d:
                    d[com] = idx
                    idx += 1
        biglist = []
        for coms in favoriteCompanies:
            cur = []
            for c in coms:
                cur.append(d[c])
            biglist.append(cur)
        #print(biglist)
        res = []
        for i in range(len(favoriteCompanies)):
            curL = favoriteCompanies[i]
            f = 0
            for j in range(len(favoriteCompanies)):
                if j == i:
                    continue
                nexL = favoriteCompanies[j]
                if len(nexL) < len(curL):
                    continue
                if self.check(curL, nexL):
                    f = 1
                    break
            if f == 0:
                res.append(i)
        return res