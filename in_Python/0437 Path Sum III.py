# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def count(arr, x):
            res = 0
            for a in arr:
                if a == x:
                    res += 1
            return res
        if not root:
            return 0
        res = 0
        q = collections.deque()
        q.append([root, [root.val]])
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                pre, L = q.popleft()
                res += count(L, sum)
                if pre.left:
                    tmp = [pre.left.val]
                    for x in L:
                        tmp.append(x + pre.left.val)
                    q.append([pre.left, tmp])
                if pre.right:
                    tmpp = [pre.right.val]
                    for x in L:
                        tmpp.append(x + pre.right.val)
                    q.append([pre.right, tmpp])
        return res
                       
        