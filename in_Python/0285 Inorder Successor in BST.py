# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        l = []
        st = []
        n = root
        while st or n:
            while n:
                st.append(n)
                n = n.left 
            x = st.pop()
            if l and l[-1] == p.val:
                return x
            l.append(x.val)
            n = x.right 
        return None
            