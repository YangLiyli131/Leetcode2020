class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        row, col = len(picture), len(picture[0])
        nr,nc = [0] * row, [0] * col
        r = 0
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B':
                    nr[i] += 1
                    nc[j] += 1
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B':
                    if nr[i] != N or nc[j] != N:
                        continue
                    currow = picture[i]
                    f = True
                    for ii in range(row):
                        if picture[ii][j] == 'B':
                            if picture[ii] != currow:
                                f = False
                                break
                    if f:
                        r += 1
        return r