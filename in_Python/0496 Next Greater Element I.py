class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        dict = {}
        for i in nums2:
            while len(stack) != 0 and i > stack[-1]:
                dict[stack[-1]] = i
                stack.pop()
            stack.append(i)
        while len(stack) != 0:
            dict[stack[-1]] = -1
            stack.pop()            
        for i in range(len(nums1)): nums1[i] = dict[nums1[i]]
        return nums1
                
        