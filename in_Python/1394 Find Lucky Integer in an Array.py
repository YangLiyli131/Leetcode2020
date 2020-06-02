class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = -1
        dict = {}
        for i in arr:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for i in dict:
            if i == dict[i]:
                res = max(res,i)
        return res