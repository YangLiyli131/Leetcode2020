class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        adjL = {}
        keys = set()
        values = set()
        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]
            values.add(left)
            values.add(right)
            tmp = []
            if left != -1:
                tmp.append(left)
            if right != -1:
                tmp.append(right)
            if len(tmp) != 0:
                adjL[i] = tmp
                keys.add(i)
        if not adjL:
            return True
        roots = []
        for i in range(n):
            if i in keys and i not in values:
                roots.append(i)
        print(roots)
        if len(roots) != 1:
            return False
        root = roots[0]
        q = [root]
        visited = set()
        visited.add(root)
        num = 0
        while q:
            h = q.pop(0)
            num += 1
            if h in adjL:
                for nex in adjL[h]:
                    if nex in visited:
                        return False
                    q.append(nex)
                    visited.add(nex)
        return num == n
        