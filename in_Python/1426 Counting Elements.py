class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        d = collections.Counter(arr)
        for k in d:
            if k+1 in d:
                res += d[k]
        return res