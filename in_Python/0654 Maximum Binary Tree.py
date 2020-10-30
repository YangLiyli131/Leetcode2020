# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None or len(nums) == 0:
            return None
        idx = 0
        maxnum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > maxnum:
                maxnum = nums[i]
                idx = i
        root = TreeNode(maxnum)
        root.left = self.constructMaximumBinaryTree(nums[0:idx])
        root.right = self.constructMaximumBinaryTree(nums[(idx+1):])
        return root