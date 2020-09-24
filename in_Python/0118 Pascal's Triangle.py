class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res
        res.append([1])
        if numRows == 1:
            return res
        res.append([1,1])
        if numRows == 2:
            return res
        for i in range(3, numRows+1):
            prev = res[-1]
            cur = []
            cur.append(1)
            for i in range(len(prev)-1):
                cur.append(prev[i] + prev[i+1])
            cur.append(1)
            res.append(cur)
        return res