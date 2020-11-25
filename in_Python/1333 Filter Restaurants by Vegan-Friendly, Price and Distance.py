class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        q = []
        heapq.heapify(q)
        for x in restaurants:
            if veganFriendly == 1:
                if x[2] == 1 and x[3] <= maxPrice and x[4] <= maxDistance:
                    cur = [-x[1],-x[0]]
                    heapq.heappush(q,cur)
            else:
                if x[3] <= maxPrice and x[4] <= maxDistance:
                    cur = [-x[1],-x[0]]
                    heapq.heappush(q,cur)
        res = []
        while q:
            cur = heapq.heappop(q)
            res.append(-cur[1])
        return res