"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        root = node
        n = node
        while n.parent:
            root = n.parent
            n = n.parent
        arr = []
        st = []
        while st or root:
            while root:
                st.append(root)
                root = root.left
            x = st.pop()
            arr.append(x)
            root = x.right 
        i = 0
        while i < len(arr):
            if arr[i].val == node.val:
                if i == len(arr)-1:
                    return None
                else:
                    break
            i += 1
        return arr[i+1]