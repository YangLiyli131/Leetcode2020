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
        while st or n:
            while n:
                st.append(n)
                n = n.left
            x = st.pop()
            self.arr.append(x.val)
            n = x.right 
        self.idx = -1      
        self.t = len(self.arr)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < self.t-1

    def next(self):
        """
        :rtype: int
        """
        if self.idx == -1:
            self.idx = 0
        else:
            self.idx += 1
        return self.arr[self.idx]
        
    def hasPrev(self):
        """
        :rtype: bool
        """
        return self.idx > 0

    def prev(self):
        """
        :rtype: int
        """
        self.idx -= 1
        return self.arr[self.idx]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()