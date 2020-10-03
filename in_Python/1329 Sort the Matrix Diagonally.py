class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(mat)
        col = len(mat[0])
        i = row-2
        while i >= 0:
            curi = i
            curj = 0
            cur = []
            while curi < row and curj < col:
                cur.append(mat[curi][curj])
                curi += 1
                curj += 1
            cur.sort()
            curi = i
            curj = 0
            while curi < row and curj < col and len(cur) != 0:
                mat[curi][curj] = cur.pop(0)
                curi += 1
                curj += 1            
            i -= 1
        j = 1
        while j < col:
            curi = 0
            curj = j
            cur = []
            while curi < row and curj < col:
                cur.append(mat[curi][curj])
                curi += 1
                curj += 1
            cur.sort()
            curi = 0
            curj = j
            while curi < row and curj < col and len(cur) != 0:
                mat[curi][curj] = cur.pop(0)
                curi += 1
                curj += 1
            j += 1
        return mat