class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        book = [0] * (n+1)
        for b in bookings:
            i = b[0]
            j = b[1]
            book[i-1] += b[2]
            book[j] -= b[2]
        for i in range(1, len(book)):
            book[i] += book[i-1]
        return book[:-1]
        