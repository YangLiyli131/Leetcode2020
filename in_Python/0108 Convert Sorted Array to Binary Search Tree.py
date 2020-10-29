# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None or len(nums) == 0:
            return None
        i,j = 0, len(nums)-1
        if i == j:
            return TreeNode(nums[i])
        m = i + (j-i)/2
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[0:m])
        root.right = self.sortedArrayToBST(nums[(m+1) : len(nums)])
        return root