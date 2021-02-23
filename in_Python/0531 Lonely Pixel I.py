class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        r = 0
        row, col = len(picture), len(picture[0])
        nr,nc = [0] * row, [0] * col
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B':
                    nr[i] += 1
                    nc[j] += 1
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B':
                    if nr[i] == 1 and nc[j] == 1:
                        r += 1
        return r