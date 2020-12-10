# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.v = set()
        root.val = 0
        q = collections.deque([root])
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.popleft()
                if h.left:
                    h.left.val = h.val * 2 + 1
                    q.append(h.left)
                if h.right:
                    h.right.val = h.val * 2 + 2
                    q.append(h.right)
                self.v.add(h.val)
        
    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.v


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)