class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for i in range(1,N+1):
            backup = i
            cur = 0
            p = 0
            flag = True
            while i != 0:
                x = i % 10
                if x in [3,4,7]:
                    flag = False
                    break
                if x == 2:
                    x = 5
                elif x == 5:
                    x = 2
                elif x == 6:
                    x = 9
                elif x == 9:
                    x = 6
                else:
                    x = x
                cur += x * (10 **p)
                p += 1
                i /= 10
            if not flag: continue
            if cur != backup: 
                res += 1
        return res