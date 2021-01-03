class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        first = collections.defaultdict(set)
        last = collections.defaultdict(set)
        res = set()
        for p in phrases:
            sts = p.split(' ')
            if sts[0] in last:
                tmp = set()
                for x in last[sts[0]]:
                    tmp.add(x + p[len(sts[0]):])
                res |= tmp
            if sts[-1] in first:
                tmp = set()
                for x in first[sts[-1]]:
                    tmp.add(p + x)
                res |= tmp
            first[sts[0]].add(p[len(sts[0]):])
            last[sts[-1]].add(p)
        return sorted(list(res))