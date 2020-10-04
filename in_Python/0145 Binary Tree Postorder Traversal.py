# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        st = []
        if root == None:
            return res
        st.append(root)
        while len(st) != 0:
            h = st.pop()
            if h.left != None:
                st.append(h.left)
            if h.right != None:
                st.append(h.right)
            res.insert(0,h.val)
        return res