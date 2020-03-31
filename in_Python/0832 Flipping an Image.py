class Solution(object):
    def iv(self,t):
        if t == 1:
            return 0
        else:
            return 1
        
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        for r in range(row):
            cur_row = A[r]
            i = 0
            j = col-1
            while i <= j:
                temp = cur_row[i]
                cur_row[i] = self.iv(cur_row[j])
                cur_row[j] = self.iv(temp)
                i += 1
                j -= 1
            A[r] = cur_row
        return A
        