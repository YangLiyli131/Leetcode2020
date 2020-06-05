class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr1 = sorted(arr)
        mindis = 10000000
        for i in range(1,len(arr)):
            curd = arr1[i] - arr1[i-1]
            if abs(curd) < mindis:
                mindis = abs(curd)
        res = []
        arrs = set(arr)
        for i in range(len(arr)):
            x = arr1[i]
            if x + mindis in arrs:
                y = x + mindis
                temp = []
                temp.append(x)
                temp.append(y)
                res.append(temp)
        return res
        