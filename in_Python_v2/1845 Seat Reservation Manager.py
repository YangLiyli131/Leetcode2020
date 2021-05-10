class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.arr = list(range(1, n+1))
        heapq.heapify(self.arr)

    def reserve(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.arr)

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.arr, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)