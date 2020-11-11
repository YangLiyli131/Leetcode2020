class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        d = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        res = []
        sign = 1
        if num < 0:
            num = -num
            sign = -1
        while num > 0:
            x = num % 16
            res.insert(0, str(x))
            num /= 16
        if sign == 1:
            for i in range(len(res)):
                if '10' <= res[i] <= '15':
                    res[i] = d[int(res[i])]
        else:
            for i in range(len(res)):
                res[i] = 15 - int(res[i])
            while len(res) != 8:
                res.insert(0,15)
            c = 0
            res[-1] += 1
            for i in range(len(res)-1,-1,-1):
                total = res[i] + c
                res[i] = total % 16
                c = total / 16
            if c != 0:
                res.insert(0,c)
            for i in range(len(res)):
                if 0 <= res[i] <= 9:
                    res[i] = str(res[i])
                else:
                    res[i] = d[res[i]]
        return ''.join(res)
            