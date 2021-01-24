class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        seq = 1
        cord = []
        i,j = 0,0
        for x in s:
            if seq == 1:
                cord.append([i,j])
                if i+1 == numRows:
                    seq = 0
                else:
                    i += 1
            else:
                i -= 1
                j += 1
                cord.append([i,j])
                if i == 0:
                    i += 1
                    seq = 1
        res = [''] * numRows
        for ci in range(len(cord)):
            c = cord[ci]
            rid = c[0]
            res[rid] += s[ci]
        return ''.join(res)
            
        