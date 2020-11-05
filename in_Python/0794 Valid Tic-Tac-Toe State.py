class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        mat = []
        for b in board:
            mat.append(list(b))
        num_o = 0
        num_x = 0
        for i in range(3):
            for j in range(3):
                if mat[i][j] == 'O':
                    num_o += 1
                elif mat[i][j] == 'X':
                    num_x += 1
        if num_o > num_x:
            return False
        if num_x - num_o > 1:
            return False
        winx = False
        wino = False
        for b in board:
            if b == 'XXX':
                winx = True
            if b == 'OOO':
                wino = True
        for j in range(3):
            curstr = ''
            for i in range(3):
                curstr += mat[i][j]
            if curstr == 'XXX':
                winx = True
            if curstr == 'OOO':
                wino = True
        first = second = ''
        for i in range(3):
            first += mat[i][i]
            second += mat[i][2-i]
        if first == 'XXX' or second == 'XXX':
            winx = True
        if first == 'OOO' or second == 'OOO':
            wino = True
        
        if wino and winx:
            return False
        if winx:
            if num_x != num_o + 1:
                return False
        if wino:
            if num_x != num_o:
                return False
        
        return True