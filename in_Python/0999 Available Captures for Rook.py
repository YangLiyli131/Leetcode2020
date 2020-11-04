class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        rowid = colid = 0
        found = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rowid = i
                    colid = j
                    found = 1
                    break
            if found:
                break
        for r in range(rowid-1, -1,-1):
            if board[r][colid] == 'B':
                break
            elif board[r][colid] == 'p':
                res += 1
                break
        for r in range(rowid+1, 8):
            if board[r][colid] == 'B':
                break
            elif board[r][colid] == 'p':
                res += 1
                break
        for c in range(colid-1,-1,-1):
            if board[rowid][c] == 'B':
                break
            elif board[rowid][c] == 'p':
                res += 1
                break
        for c in range(colid+1,8):
            if board[rowid][c] == 'B':
                break
            elif board[rowid][c] == 'p':
                res += 1
                break
        return res