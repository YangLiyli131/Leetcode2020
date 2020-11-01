class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            A = set()
            for j in range(9):
                cur = board[i][j]
                if cur != '.':
                    if cur in A:
                        return False
                    else:
                        A.add(cur)
        for i in range(9):
            A = set()
            for j in range(9):
                cur = board[j][i]
                if cur != '.':
                    if cur in A:
                        return False
                    else:
                        A.add(cur)
        coord = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for co in coord:
            left = co
            right = [co[0]+2, co[1]+2]
            A = set()
            for i in range(left[0], right[0]+1):
                for j in range(left[1], right[1]+1):
                    cur = board[i][j]
                    if cur != '.':
                        if cur in A:
                            return False
                        else:
                            A.add(cur)
        return True