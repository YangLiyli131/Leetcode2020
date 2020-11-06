# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        arr = set()
        st = []
        n = root1
        while st or n:
            while n:
                st.append(n)
                n = n.left
            x = st.pop()
            arr.add(x.val)
            n = x.right
        st = []
        n = root2
        while st or n:
            while n:
                if target - n.val in arr:
                    return True
                st.append(n)
                n = n.left
            x = st.pop()
            n = x.right
        return False
            