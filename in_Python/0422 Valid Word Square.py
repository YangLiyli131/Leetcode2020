class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        row = len(words)
        col = -1
        for w in words:
            col = max(col, len(w))
        if row != col:
            return False
        mat = []
        for i in range(row):
            mat.append([''] * col)
        for i in range(row):
            cur = words[i]
            for j in range(len(cur)):
                mat[i][j] = cur[j]
        for i in range(row):
            for j in range(col):
                a = mat[i][j]
                b = mat[j][i]
                if a == '' and b != '':
                    return False
                elif a != '' and b == '':
                    return False
                elif a != b:
                    return False
        return True
        
                