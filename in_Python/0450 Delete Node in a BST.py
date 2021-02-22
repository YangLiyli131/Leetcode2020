# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        l,r = root.left, root.right
        
        def construct(x):
            if not x:
                return None
            i,j = 0, len(x)-1
            m = i + (j-i) / 2
            r = TreeNode(x[m])
            r.left = construct(x[:m])
            r.right = construct(x[m+1:])
            return r

        if root.val == key:
            if not l and not r:
                return None
            if l and not r:
                return l
            if not l and r:
                return r
            else:
                root.left = None
                root.right = None
                la,lb = [],[]
                st = []
                a,b = l,r
                while st or a:
                    while a:
                        st.append(a)
                        a = a.left
                    x = st.pop()
                    la.append(x.val)
                    a = x.right 
                st = []
                while st or b:
                    while b:
                        st.append(b)
                        b = b.left
                    x = st.pop()
                    lb.append(x.val)
                    b = x.right

                ia,ib = 0,0
                l = []
                while ia < len(la) and ib < len(lb):
                    if la[ia] < lb[ib]:
                        l.append(la[ia])
                        ia += 1
                    else:
                        l.append(lb[ib])
                        ib += 1
                while ia < len(la):
                    l.append(la[ia])
                    ia += 1
                while ib < len(lb):
                    l.append(lb[ib])
                    ib += 1
                return construct(l)
                    
        elif root.val < key:
            root.right = self.deleteNode(r, key)
        else:
            root.left = self.deleteNode(l, key)
        return root