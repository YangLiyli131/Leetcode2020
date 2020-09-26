class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = {}
        for w in wall:
            for i in range(1, len(w)):
                w[i] = w[i-1] + w[i]
            for i in range(len(w)-1):
                if w[i] not in d:
                    d[w[i]] = 1
                else:
                    d[w[i]] += 1
        maxkey = 0
        maxcount = -1
        for k in d:
            if d[k] > maxcount:
                maxkey = k
                maxcount = d[k]
        res = 0
        #print(maxkey)
        for k in wall:
            if maxkey not in k:
                res += 1
        return res