# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        d = {}
        for i,x in enumerate(inorder):
            d[x] = i
        def recur(l,r):
            if l > r:
                return None
            m = TreeNode(postorder.pop())
            idx = d[m.val]
            m.right = recur(idx+1, r)
            m.left = recur(l,idx-1)
            return m
        return recur(0, len(inorder)-1)
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            r = postorder.pop()
            idx = -1
            for i,x in enumerate(inorder):
                if x == r:
                    idx = i
                    break
            ro = TreeNode(r)
            
            ro.right = self.buildTree(inorder[idx+1:], postorder)
            ro.left = self.buildTree(inorder[:idx], postorder)
            return ro