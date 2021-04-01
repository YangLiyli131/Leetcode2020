class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == None or len(nums) < 3:
            return False
        minarr = [-1] * len(nums)
        minarr[0] = nums[0]
        for i in range(1, len(nums)):
            minarr[i] = min(minarr[i-1], nums[i])
        st = []
        for j in range(len(nums)-1, -1, -1):
            if nums[j] <= minarr[j]:
                continue
            while st and st[-1] <= minarr[j]:
                st.pop()
            if st and st[-1] < nums[j]:
                return True
            st.append(nums[j])
        return False
            