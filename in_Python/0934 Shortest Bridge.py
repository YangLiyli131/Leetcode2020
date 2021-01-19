class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        q = collections.deque()
        row = len(A)
        col = len(A[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(A,i,j,g):
            if i < 0 or j < 0 or i >= len(A) or j >= len(A[0]) or A[i][j] != 1:
                return 
            A[i][j] = -1
            
            for d in directions:
                aa, bb = i + d[0], j + d[1]
                if aa < 0 or bb < 0 or aa >= len(A) or bb >= len(A[0]):
                    continue
                if A[aa][bb] == 0:
                    g.append((i,j))
                    break
            
            dfs(A,i-1,j,g)
            dfs(A,i+1,j,g)
            dfs(A,i,j-1,g)
            dfs(A,i,j+1,g)
        
        found = False
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    dfs(A,i,j,q)
                    found = True
                    break
            if found:
                break

        res = 0       
    
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.popleft()
                thisi, thisj = h[0],h[1]
                for d in directions:
                    nexti, nextj = thisi + d[0], thisj + d[1]
                    if 0 <= nexti < len(A) and 0 <= nextj < len(A[0]) and A[nexti][nextj] == 1:
                        return res
                    if 0 <= nexti < len(A) and 0 <= nextj < len(A[0]) and A[nexti][nextj] == 0:
                        q.append((nexti,nextj))
                        A[nexti][nextj] = -1
            res += 1
        return -1
                                 