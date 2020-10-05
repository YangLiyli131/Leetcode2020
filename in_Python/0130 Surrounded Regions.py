class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board == None:
            return board
        if len(board) == 0 or len(board[0]) == 0:
            return board
        row = len(board)
        col = len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        zeros_on_border = []
        for i in [0, row-1]:
            for j in range(col):
                if board[i][j] == 'O':
                    zeros_on_border.append([i,j])
        for j in [0, col-1]:
            for i in range(row):
                if board[i][j] == 'O' and [i,j] not in zeros_on_border:
                    zeros_on_border.append([i,j])
        while len(zeros_on_border) != 0:
            h = zeros_on_border.pop(0)
            thisi = h[0]
            thisj = h[1]
            board[thisi][thisj] = 'S'
            for d in directions:
                nexti = thisi + d[0]
                nextj = thisj + d[1]
                if 0 < nexti < row-1 and 0 < nextj < col-1:
                    if board[nexti][nextj] == 'O':
                        zeros_on_border.append([nexti,nextj])
                        board[nexti][nextj] = 'S'
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'
        
            
        