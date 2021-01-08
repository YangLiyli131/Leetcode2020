# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        res = set()
        st = [[root, [root.val]]]
        while st:
            n, l = st.pop()
            if not n.left and not n.right:
                res.add(tuple(l))
            else:
                if n.left:
                    st.append([n.left, l + [n.left.val]])
                if n.right:
                    st.append([n.right, l + [n.right.val]])
        return tuple(arr) in res
        