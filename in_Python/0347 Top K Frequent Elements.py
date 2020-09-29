class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        q = []
       # heapq.heapify(q)
        for key in d:
            t = (d[key],key)
            heappush(q,t)
        res = []
        while len(q) > k:
            heappop(q)
        while len(q) != 0:
            g = heappop(q)
            #print(g)
            res.insert(0, g[1])
        return res