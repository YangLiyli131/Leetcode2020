# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        st = []
        res = []
        if root == None:
            return res
        st.append([root,""])
        while st:
            n, s = st.pop()
            if n.left == None and n.right == None:
                res.append(s + str(n.val))
            if n.right != None:
                st.append([n.right, s + str(n.val) + '->'])
            if n.left != None:
                st.append([n.left, s + str(n.val) + '->'])
        return res