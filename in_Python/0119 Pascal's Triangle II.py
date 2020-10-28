class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n = rowIndex
        if n == 0:
            return [1]
        res1 = [1]
        res2 = [1]
        if n == 1:
            return res1 + res2
        for i in range(1, n/2):
            if i == 1:
                res1.append(n)
                res2.insert(0,n)
            else:
                prev = res1[-1]
                cur = prev * (n - i + 1) / i
                res1.append(cur)
                res2.insert(0,cur)
        prev = res1[-1]
        cur = prev * (n - n/2 + 1) / (n/2)
        if n % 2 == 1:
            res2.insert(0,cur)
        res1.append(cur)
        return res1 + res2