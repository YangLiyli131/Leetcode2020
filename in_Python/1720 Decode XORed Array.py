class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        res = [first]
        for x in encoded:
            tmp = x ^ res[-1]
            res.append(tmp)
        return res
        