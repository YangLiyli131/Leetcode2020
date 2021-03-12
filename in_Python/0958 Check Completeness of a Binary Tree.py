# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = collections.deque()
        q.append(root)
        l = -1
        levels = []
        while q:
            n = len(q)
            cur = []
            while n != 0:
                n -= 1
                h = q.popleft()
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
                cur.append(h)
            levels.append(cur)
            l += 1
        for i in range(len(levels)-1):
            if len(levels[i]) != 2 **i:
                return False
        if len(levels[-1]) == 2 ** l:
            return True
        last = []
        if l == 0:
            return len(levels[0]) == 1
        for x in levels[-2]:
            if x.left:
                last.append(x.left.val)
            else:
                last.append(-1)
            if x.right:
                last.append(x.right.val)
            else:
                last.append(-1)
        lastvalid, firstminusid = -1,-1
        for i in range(len(last)):
            if last[i] != -1:
                lastvalid = i
            if last[i] == -1 and firstminusid == -1:
                firstminusid = i
        return lastvalid < firstminusid
            