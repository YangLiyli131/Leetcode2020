class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        direc = [[1,0],[-1,0],[0,1],[0,-1]]
        row,col = len(isWater), len(isWater[0])
        r = []
        for i in range(row):
            r.append([-1] * col)
        q = collections.deque()
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    r[i][j] = 0
                    q.append((i,j))
        while q:
            curi, curj = q.popleft()
            for d in direc:
                nexti,nextj = curi + d[0], curj + d[1]
                if 0 <= nexti < row and 0 <= nextj < col and r[nexti][nextj] < 0:
                    r[nexti][nextj] = r[curi][curj] + 1
                    q.append((nexti,nextj))

        return r
                
            
            