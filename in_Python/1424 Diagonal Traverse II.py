class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        d = {}
        res = []
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(len(cur)):
                s = i + j
                v = [i,cur[j]]
                if s not in d:
                    d[s] = [v]
                else:
                    d[s].append(v)
        keys = d.keys()
        keys.sort()
        for k in keys:
            cur = d[k]
            cur.sort(reverse = True)
            for c in cur:
                res.append(c[1])
        return res