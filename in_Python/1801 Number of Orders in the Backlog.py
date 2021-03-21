class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        bu,se = [], []
        for x in orders:
            a,b,t = x[0],x[1],x[2]
            n = b
            if t == 0:
                while n > 0 and se:
                    p,num = heapq.heappop(se)
                    if p > a:
                        heapq.heappush(se, [p, num])
                        break
                    if num <= n:
                        n -= num
                    else:
                        heapq.heappush(se, [p, num-n])
                        n = 0
                if n > 0:
                    heapq.heappush(bu,[-a,n])
            else:
                while n > 0 and bu:
                    p, num = heapq.heappop(bu)
                    if -p < a:
                        heapq.heappush(bu, [p, num])
                        break
                    if num <= n:
                        n -= num
                    else:
                        heapq.heappush(bu, [p, num-n])
                        n = 0
                if n > 0:
                    heapq.heappush(se,[a,n])
        r = 0
        for x in bu:
            r += x[1]
        for x in se:
            r += x[1]
        return r % 1000000007
            