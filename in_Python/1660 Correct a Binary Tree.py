# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def correctBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []
        st = [root]
        error = None
        while st:
            h = st.pop()
            if h.left:
                st.append(h.left)
            if h.right:
                st.append(h.right)
            if h.right and h.right.val in arr:
                error = h
                break
            arr.insert(0, h.val)
        
        q = [root]
        while q:
            nn = len(q)
            while nn != 0:
                nn -= 1
                n = q.pop(0)
                if n.left and n.left == h:
                    n.left = None
                    return root
                if n.right and n.right == h:
                    n.right = None
                    return root
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        
        return root
        
        