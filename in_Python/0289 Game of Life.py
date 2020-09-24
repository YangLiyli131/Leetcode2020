class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == 0:
                    board[i][j] = 'D'
                else:
                    board[i][j] = 'L'
        for i in range(row):
            for j in range(col):
                curstate = board[i][j]
                living_nei = 0
                for ni in [i-1, i, i+1]:
                    for nj in [j-1, j, j+1]:
                        if ni == i and nj == j:
                            continue
                        if ni < 0 or ni >= row:
                            continue
                        if nj < 0 or nj >= col:
                            continue
                        x = board[ni][nj]
                        if x[0] == 'L':
                            living_nei += 1
                if curstate[0] == 'L':
                    if living_nei < 2 or living_nei > 3:
                        curstate += 'D'
                    else:
                        curstate += 'L'
                if curstate[0] == 'D':
                    if living_nei == 3:
                        curstate += 'L'
                    else:
                        curstate += 'D'
                board[i][j] = curstate
        #print(board)
        for i in range(row):
            for j in range(col):
                curstate = board[i][j]
                if curstate[1] == 'L':
                    board[i][j] = 1
                else:
                    board[i][j] = 0