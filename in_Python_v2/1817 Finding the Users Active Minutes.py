class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for x in logs:
            a,b = x[0], x[1]
            if a not in d:
                d[a] = set()
            d[a].add(b)
        dd = {}
        for x in d:
            v = len(d[x])
            if v not in dd:
                dd[v] = 0
            dd[v] += 1
        r = []
        for i in range(1, k+1):
            if i not in dd:
                r.append(0)
            else:
                r.append(dd[i])
        return r