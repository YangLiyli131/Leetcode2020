# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        res = []
        idx = 0
        if root == None:
            return res
        q.append(root)
        while len(q) != 0:
            n = len(q)
            cur = []
            for i in range(n):
                head = q.pop(0)
                if head.left != None:
                    q.append(head.left)
                if head.right != None:
                    q.append(head.right)
                if idx == 0:
                    cur.append(head.val)
                else:
                    cur.insert(0, head.val)
            if idx == 0:
                idx = 1
            else:
                idx = 0
            res.append(cur)
        return res