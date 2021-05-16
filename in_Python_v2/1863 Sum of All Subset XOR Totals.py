class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = sum(nums)
        n = len(nums)
        l = []
        for i in range(n):
            l.append([i])
        L = [l]
        added = True
        while added:
            added = False
            pre = L[-1]
            t = []
            for x in pre:
                for i in range(n):
                    if i not in x and i > max(x):
                        added = True
                        xx = x + [i]
                        t.append(xx)
                        z = nums[xx[0]]
                        for zz in xx[1:]:
                            z = z ^ nums[zz]
                        r += z
            L.append(t)
        return r