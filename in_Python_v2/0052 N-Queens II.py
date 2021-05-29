class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def bt(row, diag, adiag, cols):
            if row == n:
                return 1
            sol = 0
            for col in range(n):
                cur_diag = row - col
                cur_adiag = row + col
                if (col in cols or cur_diag in diag or cur_adiag in adiag):
                    continue
                cols.add(col)
                diag.add(cur_diag)
                adiag.add(cur_adiag)
                sol += bt(row+1, diag, adiag, cols)
                cols.remove(col)
                diag.remove(cur_diag)
                adiag.remove(cur_adiag)
            return sol
        return bt(0, set(), set(), set())