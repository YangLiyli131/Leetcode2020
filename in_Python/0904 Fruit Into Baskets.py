class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        res = 0
        i,j = 0,0
        d = {}
        for i in range(len(tree)):
            x = tree[i]
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
            while j < len(tree) and len(d) > 2:
                y = tree[j]
                d[y] -= 1
                if d[y] == 0:
                    del d[y]
                j += 1
            res = max(res, i-j+1)
        return res