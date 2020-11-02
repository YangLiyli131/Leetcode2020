class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        scores = {}
        for it in items:
            idx = it[0]
            v = it[1]
            if idx not in scores:
                scores[idx] = [-v]
            else:
                heapq.heappush(scores[idx],-v)
        res = []
        keys = scores.keys()
        keys.sort()
        for k in keys:
            total = 0
            row = scores[k]
            if len(row) <= 5:
                res.append([k, -sum(row) / len(row)])
            else:
                t = 5
                while t != 0:
                    t -= 1
                    total -= heapq.heappop(row)
                res.append([k, total/5])
        return res
        
        