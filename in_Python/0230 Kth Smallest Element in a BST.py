# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        st = []
        n = root
        while n or st:
            while n:
                st.append(n)
                n = n.left
            n = st.pop()
            heappush(res, n.val)
            n = n.right
        #print(res)
        q = []
        while k != 0:
            heappush(q, heappop(res))
            k -= 1
        #print(q)
        return q[-1]
        
            