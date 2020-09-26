class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        xx = []
        yy = []
        if x == 1:
            xx = [1,1]
        if y == 1:
            yy = [1,1]
        i = 0
        while x != 1 and pow(x,i) <= bound:
            xx.append(pow(x,i))
            i += 1
        i = 0
        while y != 1 and pow(y,i) <= bound:
            yy.append(pow(y,i))
            i += 1
        res = []
        for i in xx:
            for j in yy:
                d = i + j
                if d not in res and d <= bound:
                    res.append(d)
        return res