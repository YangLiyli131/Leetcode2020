# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 1
        dq = collections.deque()
        dq.appendleft([root,1])
        while dq:
            for i in range(len(dq)):
                top = dq.pop()
                if top[0].left:
                    dq.appendleft([top[0].left, 2 * top[1] - 1])
                if top[0].right:
                    dq.appendleft([top[0].right, 2 * top[1]])
            if len(dq) == 0:
                break
            res = max(res, dq[0][1] - dq[-1][1] + 1)
        return res