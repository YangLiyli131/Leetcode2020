class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.q = nums
        self.n = k
        heapq.heapify(self.q)
        while len(self.q) > k:
            heapq.heappop(self.q)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.q) < self.n:
            heapq.heappush(self.q, val)
        elif val > self.q[0]:
            heapq.heapreplace(self.q, val)
        return self.q[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)