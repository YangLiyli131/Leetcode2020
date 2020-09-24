class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        if row * col != r * c:
            return nums
        alln = []
        for i in range(row):
            for j in range(col):
                alln.append(nums[i][j])
        res = []
        for i in range(r):
            cs = []
            for j in range(c):
                cs.append(0)
            res.append(cs)
        idx = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = alln[idx]
                idx += 1
        return res