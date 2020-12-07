# Definition for Node.
# class Node(object):
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution(object):
    def copyRandomBinaryTree(self, root):
        """
        :type root: Node
        :rtype: NodeCopy
        """
        if not root:
            return None
        d = {root : NodeCopy(root.val)}
        q = collections.deque([root])
        while q:
            h = q.popleft()
            if h.left:
                if h.left not in d:
                    d[h.left] = NodeCopy(h.left.val)
                    q.append(h.left)
                d[h].left = d[h.left]
            if h.right:
                if h.right not in d:
                    d[h.right] = NodeCopy(h.right.val)
                    q.append(h.right)
                d[h].right = d[h.right]
            if h.random:
                if h.random not in d:
                    d[h.random] = NodeCopy(h.random.val)
                    q.append(h.random)
                d[h].random = d[h.random]
        return d[root]