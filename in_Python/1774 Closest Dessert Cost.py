class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        top_combo = {0}
        for x in toppingCosts:
            temp = top_combo.copy()
            for y in top_combo:
                temp.add(x+y)
                temp.add(x+x+y)
            top_combo = temp
        r = []
        md = sys.maxint
        for b in baseCosts:
            for t in top_combo:
                d = abs(b + t - target)
                if d < md:
                    md = d
                    r = [b + t]
                elif d == md:
                    r.append(b+t)
        r.sort()
        return r[0]
            