class Solution(object):
    def count(self,n):
        res = 0
        while n != 0:
            res += n % 2
            n /= 2
        return res
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = set()
        for h in range(12):
            a = self.count(h)
            for m in range(60):
                b = self.count(m)
                if a + b == num:
                    tmp = str(h) + ':'
                    if m < 10:
                        tmp += '0'
                    tmp += str(m)
                    res.add(tmp)
        return list(res)
                    