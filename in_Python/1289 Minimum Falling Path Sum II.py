class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        row, col = len(arr), len(arr[0])
        for i in range(1, row):
            for j in range(col):
                pre = arr[i-1]
                arr[i][j] += min(pre[:j] + pre[j+1:])
        return min(arr[-1])