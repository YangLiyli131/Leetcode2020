class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        def check(a,b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])
        s = sum(2*check(tree, x) for x in nuts)
        return min(s + check(squirrel,x) - check(tree,x) for x in nuts)
        