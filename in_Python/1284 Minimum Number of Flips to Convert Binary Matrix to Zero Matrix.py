class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m,n = len(mat), len(mat[0])
        r = 0
        
        def check(m):
            s = 0
            for i in range(len(m)):
                for j in range(len(m[0])):
                    s += m[i][j]
            return s != 0
        
        if not check(mat):
            return 0
        
        def flip(matt, i,j):
            mat = []
            for k in range(len(matt)):
                mat.append(matt[k][:])
            cur = matt[i][j]
            mat[i][j] = 1 - cur
            if 0 <= i-1 < len(mat):
                mat[i-1][j] = 1 - mat[i-1][j]
            if 0 <= i+1 < len(mat):
                mat[i+1][j] = 1 - mat[i+1][j]
            if 0 <= j-1 < len(mat[0]):
                mat[i][j-1] = 1 - mat[i][j-1]
            if 0 <= j+1 < len(mat[0]):
                mat[i][j+1] = 1 - mat[i][j+1]
            return mat
        
        q = collections.deque()
        q.append([mat, []])
        while q:
            L = len(q)
            r += 1
            while L != 0:
                L -= 1
                mxx, pre = q.popleft()
                
                for i in range(m):
                    for j in range(n):
                        if (i,j) in pre:
                            continue
                        mx = []
                        for k in range(m):
                            mx.append(mxx[k][:])
                        newmatrix = flip(mx, i, j)
                        if not check(newmatrix):
                            return r
                        newpre = pre[:]
                        newpre.append((i,j))
                        q.append([newmatrix, newpre])
        return -1