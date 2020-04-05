class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        temp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            temp.append(row)
        for i in range(m):
            temp[i][0] = 1
        for i in range(n):
            temp[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                temp[i][j] = temp[i-1][j] + temp[i][j-1]
        return temp[m-1][n-1]
            
        