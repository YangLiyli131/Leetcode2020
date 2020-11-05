class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.size = n
        self.mat = []
        for i in range(n):
            self.mat.append([0] * n)

    def checkrow(self, p, row):
        total = sum(self.mat[row])
        if p == 1 and total == self.size:
            return True
        if p == 2 and total == -self.size:
            return True
        return False
    
    def checkcol(self, p, col):
        total = 0
        for i in range(self.size):
            total += self.mat[i][col]
        if p == 1 and total == self.size:
            return True
        if p == 2 and total == -self.size:
            return True
        return False
    
    def checkdiag(self,p):
        first = second = 0
        for i in range(self.size):
            first += self.mat[i][i]
            second += self.mat[i][self.size - i - 1]
        if p == 1:
            if first == self.size or second == self.size:
                return True
        else:
            if first == -self.size or second == -self.size:
                return True
        return False
    
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            self.mat[row][col] = 1
        else:
            self.mat[row][col] = -1
        if self.checkrow(player,row) or self.checkcol(player,col):
                return player
        if row == col or row + col == self.size-1:
            if self.checkdiag(player):
                return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)