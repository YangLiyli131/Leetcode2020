class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        prex = [0]
        for x in nums:
            prex.append(prex[-1] + x)
        j,k = 0,0
        for i in range(1, len(nums)):
            j = max(j, i+1)
            while j < len(nums) and 2 * prex[i] > prex[j]:
                j += 1
            k = max(k, j)
            while k < len(nums) and prex[k] - prex[i] <= prex[-1] - prex[k]:
                k += 1
            res += k - j
        return res % (pow(10,9)+7)
            

        