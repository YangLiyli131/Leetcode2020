class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        x = [nums[0]]
        for i in range(1,n):
            x.append(x[-1] + nums[i])
        re = []
        for i in x:
            re.append(i)
        for j in range(n-1,0,-1):
            cur = x[j]
            for i in range(j-1,-1,-1):
                re.append(cur - x[i])
        re.sort()
        s = 0
        for i in range(left-1, right):
            s += re[i]
        return s % (pow(10,9)+7)
                