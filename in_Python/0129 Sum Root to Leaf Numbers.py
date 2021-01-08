# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        st = []
        res = 0
        if not root:
            return res
        st.append([root, root.val])
        while st:
            n, v = st.pop()
            if not n.left and not n.right:
                res += v
            else:
                if n.left:
                    st.append([n.left, v * 10 + n.left.val])
                if n.right:
                    st.append([n.right, v * 10 + n.right.val])
        return res
        