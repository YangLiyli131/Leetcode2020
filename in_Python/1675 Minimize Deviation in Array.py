class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q = []
        res = sys.maxint
        ma = -sys.maxint
        for n in nums:
            cur = n
            while n % 2 == 0:
                n /= 2
            heapq.heappush(q, [n, cur])
            ma = max(ma, n)
        while len(q) == len(nums):
            a, b = heapq.heappop(q)
            res = min(res, ma - a)
            if a % 2 == 1 or a < b:
                ma = max(ma, a * 2)
                heapq.heappush(q, [a*2, b])
        return res
        