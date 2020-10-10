class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        for i in range(1, len(nums)):
            self.arr[i] += self.arr[i-1]
        self.arr.insert(0,0)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.arr[j+1] - self.arr[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)