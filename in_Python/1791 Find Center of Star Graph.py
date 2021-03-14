class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        d = set()
        for x in edges:
            a,b = x[0],x[1]
            if a in d:
                return a
            if b in d:
                return b
            d.add(a)
            d.add(b)
        return None