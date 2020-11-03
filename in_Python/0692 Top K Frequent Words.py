class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = {}
        for w in words:
            if w not in counter:
                counter[w] = 1
            else:
                counter[w] += 1
        x = {}
        for ky in counter:
            v = counter[ky]
            if v not in x:
                x[v] = [ky]
            else:
                x[v].append(ky)
        q = []
        for ky in x.keys():
            q.append(-ky)
        heapq.heapify(q)
        res = []
        while q:
            cur = heapq.heappop(q)
            row = x[-cur]
            row.sort()
            for y in row:
                res.append(y)
                k -= 1
                if k == 0:
                    return res
        return res
            