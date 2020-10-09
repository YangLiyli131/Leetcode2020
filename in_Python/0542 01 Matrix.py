class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    continue
                count = 0
                q = []
                q.append([i,j])
                found = 0
                while q:
                    l = len(q)
                    while l != 0:
                        l -= 1
                        cur = q.pop(0)
                        thisi = cur[0]
                        thisj = cur[1]
                        for d in directions:
                            nexti = thisi + d[0]
                            nextj = thisj + d[1]
                            if 0 <= nexti < row and 0 <= nextj < col:
                                if matrix[nexti][nextj] == 0:
                                    found = 1
                                    break
                                else:
                                    q.append([nexti,nextj])
                    count += 1
                    if found:
                        break
                matrix[i][j] = count
        return matrix
                
                     