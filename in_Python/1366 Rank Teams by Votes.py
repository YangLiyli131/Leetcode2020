class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        L = len(votes[0])
        d = {}
        for v in votes[0]:
            d[v] = [0] * L
        for v in votes:
            for i in range(len(v)):
                cur = v[i]
                d[cur][i] += 1
        for k in d:
            d[k] = tuple(d[k])
        counter = {}
        for k in d:
            c = d[k]
            if c not in counter:
                counter[c] = [k]
            else:
                counter[c].append(k)
        res = []
        keys = counter.keys()
        keys.sort(reverse = True)
        for k in keys:
            nex = counter[k]
            if len(nex) == 1:
                res.append(nex[0])
            else:
                nex.sort()
                for nx in nex:
                    res.append(nx)
        return ''.join(res)