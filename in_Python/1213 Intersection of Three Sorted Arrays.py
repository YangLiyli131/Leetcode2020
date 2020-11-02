class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in arr1:
            d[i] = 1
        for i in arr2:
            if i in d:
                d[i] += 1
        for i in arr3:
            if i in d:
                d[i] += 1
        res = []
        for k in d:
            if d[k] == 3:
                res.append(k)
        res.sort()
        return res