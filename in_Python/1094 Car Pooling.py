class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        arr = []
        for n,i,j in trips:
            arr.append([i,n])
            arr.append([j,-n])
        arr.sort()
        cap = 0
        for a in arr:
            cap += a[1]
            if cap > capacity:
                return False
        return True