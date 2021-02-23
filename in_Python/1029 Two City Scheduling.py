class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        a,b = [],[]
        c = sorted(costs, key = lambda x : abs(x[1] - x[0]), reverse = True)
        for cc in c:
            x,y = cc[0], cc[1]
            if x < y:
                if len(a) < n/2:
                    a.append(x)
                else:
                    b.append(y)
            else:
                if len(b) < n/2:
                    b.append(y)
                else:
                    a.append(x)
        return sum(a) + sum(b)