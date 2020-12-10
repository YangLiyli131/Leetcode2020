class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def helper(board, i, j):
            while i + 1 < len(board) and board[i+1][j] == 'X':
                board[i+1][j] = 'S'
                i += 1
            while j + 1 < len(board[0]) and board[i][j+1] == 'X':
                board[i][j+1] = 'S'
                j += 1    
        res = 0
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    res += 1
                    helper(board, i, j)
        return res