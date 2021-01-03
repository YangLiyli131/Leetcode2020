class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        d = {}
        for x in boxTypes:
            a = x[0]
            b = x[1]
            if b not in d:
                d[b] = a
            else:
                d[b] += a
        res = 0
        k = d.keys()
        k.sort(reverse = True)
        for key in k:
            v = d[key]
            if truckSize <= v:
                res += key * truckSize
                return res
            else:
                res += key * v
                truckSize -= v
        return res