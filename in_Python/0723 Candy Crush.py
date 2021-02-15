class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])
        def check(b,i,j):
            v = b[i][j]
            if v == 0:
                return False
            if 0 <= i-2 < m and 0 <= i-1 < m:
                if abs(b[i-2][j]) == v and abs(b[i-1][j]) == v:
                    return True
            if 0 <= i+2 < m and 0 <= i+1 < m:
                if abs(b[i+2][j]) == v and abs(b[i+1][j]) == v:
                    return True
            if 0 <= i-1 < m and 0 <= i+1 < m:
                if abs(b[i-1][j]) == v and abs(b[i+1][j]) == v:
                    return True
            if 0 <= j-2 < n and 0 <= j-1 < n:
                if abs(b[i][j-2]) == v and abs(b[i][j-1]) == v:
                    return True
            if 0 <= j+2 < n and 0 <= j+1 < n:
                if abs(b[i][j+2]) == v and abs(b[i][j+1]) == v:
                    return True
            if 0 <= j-1 < n and 0 <= j+1 < n:
                if abs(b[i][j-1]) == v and abs(b[i][j+1]) == v:
                    return True
            return False
        
        f = True
        while f:
            f = False
            for i in range(m):
                for j in range(n):
                    if check(board, i, j):
                        f = True
                        if board[i][j] > 0:
                            board[i][j] = -board[i][j]
            for i in range(m):
                for j in range(n):
                    if board[i][j] < 0:
                        board[i][j] = 0
            for j in range(n):
                curcol = []
                for i in range(m-1, -1, -1):
                    if board[i][j] != 0:
                        curcol.append(board[i][j])
                ll = len(curcol)
                while ll != m:
                    curcol.append(0)
                    ll += 1
                for i in range(m-1,-1,-1):
                    board[i][j] = curcol[m-1-i]
        return board
        