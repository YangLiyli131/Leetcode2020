class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        d = {}
        for i in range(len(colors)):
            c = colors[i]
            if c not in d:
                d[c] = [i]
            else:
                d[c].append(i)
        for k in d:
            tmp = d[k]
            tmp.sort()
            d[k] = tmp
        rr = []
        for q in queries:
            idx = q[0]
            c = q[1]
            if c not in d:
                rr.append(-1)
                continue
            if idx <= d[c][0]:
                rr.append(d[c][0] - idx)
                continue
            if idx >= d[c][-1]:
                rr.append(idx-d[c][-1])
                continue
            l = bisect.bisect_left(d[c], idx)
            r = bisect.bisect_right(d[c], idx)-1
            rr.append(min(abs(d[c][l]-idx), abs(d[c][r]-idx)))
        return rr