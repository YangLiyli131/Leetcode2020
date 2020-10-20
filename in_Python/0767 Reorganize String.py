class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        d = {}
        for s in S:
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1
        q = []
        for k in d:
            q.append((-d[k],k))
        heapq.heapify(q)
        pre_a,pre_b = 0,''
        res = []
        while q:
            a,b = heapq.heappop(q)
            res.append(b)
            if pre_a < 0:
                heapq.heappush(q, (pre_a, pre_b))
            a += 1
            pre_a = a
            pre_b = b
        res = ''.join(res)
        if len(S) != len(res):
            return ''
        return res