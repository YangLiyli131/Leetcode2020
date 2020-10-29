# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.arr = []
        st = []
        n = root
        while n or st:
            while n != None:
                st.append(n)
                n = n.left
            n = st.pop()
            self.arr.append(n.val)
            n = n.right
        self.idx = 0

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext():
            res = self.arr[self.idx]
            self.idx += 1
            return res

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.idx < len(self.arr)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()