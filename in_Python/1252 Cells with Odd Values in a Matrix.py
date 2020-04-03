class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        row_dict = {}
        col_dict = {}
        for i in range(n):
            row_dict[i] = 0
        for i in range(m):
            col_dict[i] = 0
            
        for idx in indices:
            rid = idx[0]
            cid = idx[1]
            row_dict[rid] += 1
            col_dict[cid] += 1    
        res = 0
        for x in row_dict.values():
            for y in col_dict.values():
                if (x + y) % 2 == 1:
                    res += 1
        return res
        