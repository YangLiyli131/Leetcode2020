class Solution(object):
    def count(self, board, i, j):
        directions = [[1,0],[-1,0],[1,1],[1,-1],[0,1],[0,-1],[-1,-1],[-1,1]]
        mines = 0
        for d in directions:
            nexti, nextj = i + d[0], j + d[1]
            if 0 <= nexti < len(board) and 0 <= nextj < len(board[0]):
                if board[nexti][nextj] == 'M':
                    mines += 1
        return mines
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        i,j = click[0],click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        directions = [[1,0],[-1,0],[1,1],[1,-1],[0,1],[0,-1],[-1,-1],[-1,1]]
        mines = self.count(board, i, j)
        boardcopy = board[:][:]
        if mines != 0:
            board[i][j] = str(mines)
            return board
        else:
            board[i][j] = 'B'
            q = collections.deque()
            q.append([i,j])
            seen = set()
            while q:
                pre = q.popleft()
                x = pre[0]
                y = pre[1]
                seen.add((x,y))
                for d in directions:
                    nextx, nexty = x + d[0], y + d[1]
                    if 0 <= nextx < len(board) and 0 <= nexty < len(board[0]) and (nextx,nexty) not in seen:
                        seen.add((nextx, nexty))
                        if board[nextx][nexty] != 'E':
                            continue
                        value = self.count(boardcopy, nextx, nexty)
                        if value == 0:
                            board[nextx][nexty] = 'B'
                            q.append([nextx, nexty])
                        else:
                            board[nextx][nexty] = str(value)
            
        return board
        