class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        def flip(a):
            aa = a[:][:]
            i,j = 0, len(a)-1
            while i < j:
                for r in range(len(a)):
                    t = aa[r][i]
                    aa[r][i] = aa[r][j]
                    aa[r][j] = t
                i += 1
                j -= 1
            return aa
        
        def tra(a):
            r = a[:][:]
            for i in range(len(a)):
                for j in range(i+1, len(a)):
                    t = r[i][j]
                    r[i][j] = r[j][i]
                    r[j][i] = t
            return flip(r)
        def same(a,b):
            for i in range(len(a)):
                for j in range(len(b)):
                    if a[i][j] != b[i][j]:
                        return False
            return True
        if same(mat, target):
            return True
        if same(tra(mat), target) or same(tra(tra(mat)), target) or same(tra(tra(tra(mat))), target):
            return True
        return False
        
                