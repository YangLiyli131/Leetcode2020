class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        d = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                cur = mat[i][j]
                if cur in d:
                    d[cur] += 1
                else:
                    d[cur] = 1
        res = []
        for k in d:
            if d[k] == len(mat):
                res.append(k)
        res.sort()
        if len(res) == 0:
            return -1
        return res[0]
        