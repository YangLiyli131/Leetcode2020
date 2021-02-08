# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []
        st = []
        n = root
        while st or n:
            while n:
                st.append(n)
                n = n.left
            x = st.pop()
            arr.append(x.val)
            n = x.right 
        
        def helper(arr):
            if not arr:
                return None
            n = len(arr)
            nr = TreeNode(arr[n/2])
            nr.left = helper(arr[:n/2])
            nr.right = helper(arr[n/2+1:])
            return nr
        return helper(arr)
        
        