class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        for ni in range(len(num2)-1, -1, -1):
            b = num2[ni]
            curres = []
            c = 0
            for nj in range(len(num1)-1, -1, -1):
                a = num1[nj]
                m = int(a) * int(b) + c
                curres.insert(0, m % 10)
                c = m / 10
            if c != 0:
                curres.insert(0, c)
            r = 0
            p = 0
            
            while len(curres) != 0:
                z = curres.pop()
                r += z * pow(10,p)
                p += 1
            #print(r)
            res.append(r)
        result = 0
        p = 0
        #print(res)
        while len(res) != 0:
            z = res.pop(0)
            result += z * pow(10,p)
            p += 1
        return str(result)
                