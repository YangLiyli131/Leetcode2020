class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        rowsum = []
        d = {}
        for rd in range(len(mat)):
            row = mat[rd]
            cs = 0
            i = 0
            while i < len(row) and row[i] == 1:
                cs += 1
                i += 1
            if cs not in d:
                t = []
                t.append(rd)
                d[cs] = t
            else:
                t = d[cs]
                t.append(rd)
                d[cs] = t
        rs = []
        for kk in d:
            rs.append(kk)
        rs.sort()
        allid = []
        for i in rs:
            ii = d[i]
            for iii in ii:
                allid.append(iii)
        return allid[0:k]