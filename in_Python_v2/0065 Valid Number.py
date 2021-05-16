# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        arr = []
        q = collections.deque()
        q.append(root)
        while q:
            h = q.popleft()
            if h.right:
                q.appendleft(h.right)
            if h.left:
                q.appendleft(h.left)
            arr.append(h.val)
        root.left = None
        if len(arr) == 1:
            return 
        root.right = TreeNode(arr[1])
        n = root.right
        for x in arr[2:]:
            n.right = TreeNode(x)
            n = n.right
        
        