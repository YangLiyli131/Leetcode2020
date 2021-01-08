# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = 0
        st = [[root,1]]
        while st:
            node, level = st.pop()
            if not node.left and not node.right:
                height = max(height, level)
            else:
                if node.left:
                    st.append([node.left, level+1])
                if node.right:
                    st.append([node.right, level+1])
        width = pow(2, height) - 1
        row = [None] * width
        row[width/2] = root
        res = []
        res.append(row)
        height -= 1
        while height != 0:
            w = pow(2, height) - 1
            w = (w-1) / 2 + 1
            height -= 1
            pre = res[-1]
            cur = [None] * width
            for i in range(width):
                if pre[i]:
                    left = i - w
                    right = i + w
                    cur[left] = pre[i].left
                    cur[right] = pre[i].right
            res.append(cur)
        results = []
        for x in res:
            cur = []
            for xi in x:
                if xi == None:
                    cur.append('')
                else:
                    cur.append(str(xi.val))
            results.append(cur)
        return results
        
        