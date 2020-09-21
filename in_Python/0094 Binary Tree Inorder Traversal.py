# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        st = []
        n = root
        while n != None or len(st) != 0:
            while n != None:
                st.append(n)
                n = n.left
            n = st.pop()
            res.append(n.val)
            n = n.right
        return res