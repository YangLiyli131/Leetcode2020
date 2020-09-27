class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in arr1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        res = []
        for i in arr2:
            if i in d:
                n = d[i]
                while n != 0:
                    res.append(i)
                    n -= 1
                d.pop(i, d[i])
        remain = []
        for k in d:
            remain.append(k)
        remain.sort()
        for r in remain:
            n = d[r]
            while n != 0:
                res.append(r)
                n -= 1
        return res
        