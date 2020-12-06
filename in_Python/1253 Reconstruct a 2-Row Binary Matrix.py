class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n = len(colsum)
        res = []
        for i in range(2):
            res.append([0] * n)
        for i in range(n):
            cur = colsum[i]
            if cur == 0:
                continue
            elif cur == 2:
                if upper < 1 or lower < 1:
                    return []
                upper -= 1
                lower -= 1
                res[0][i] = 1
                res[1][i] = 1
            else:
                if upper == lower == 0:
                    return []
                if upper >= lower:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
        if upper != 0 or lower != 0:
            return []
        return res
