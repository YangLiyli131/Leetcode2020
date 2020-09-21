# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        if root == None:
            return stack
        stack.append(root)
        while len(stack) != 0:
            cur_node = stack.pop()
            res.append(cur_node.val)
            if cur_node.right != None:
                stack.append(cur_node.right)
            if cur_node.left != None:
                stack.append(cur_node.left)            
        return res