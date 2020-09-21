class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}
        for i in target:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1
        for j in arr:
            if j not in dict:
                return False
            else:
                dict[j] = dict[j] - 1
        for key in dict:
            if dict[key] != 0:
                return False
        return True