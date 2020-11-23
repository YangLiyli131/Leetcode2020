# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if root == None:
                return [0,0]
            left = helper(root.left)
            right = helper(root.right)
            tmp = [0,0]
            tmp[0] = max(left[0], left[1]) + max(right[0], right[1])
            tmp[1] = root.val + left[0] + right[0]
            return tmp
        
        res = helper(root)
        return max(res[0], res[1])