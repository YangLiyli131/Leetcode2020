class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        hq = []
        heapq.heappush(hq, -matrix[0][0])
        for i in range(1, col):
            matrix[0][i] = matrix[0][i] ^ matrix[0][i-1]
            heapq.heappush(hq, -matrix[0][i])
        for i in range(1, row):
            matrix[i][0] = matrix[i][0] ^ matrix[i-1][0]
            heapq.heappush(hq, -matrix[i][0])
        for i in range(1, row):
            for j in range(1, col):
                matrix[i][j] = matrix[i][j] ^ matrix[i-1][j] ^ matrix[i][j-1] ^ matrix[i-1][j-1]
                heapq.heappush(hq, -matrix[i][j])
        while k != 1:
            k -= 1
            heapq.heappop(hq)
        return -heapq.heappop(hq)
                
                