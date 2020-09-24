class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        i = len(num1) - 1
        j = len(num2) - 1
        c = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                a = int(num1[i])
            else:
                a = 0
            if j >= 0:
                b = int(num2[j])
            else:
                b = 0
            s = a + b + c
            res.insert(0, s % 10)
            c = s / 10
            i -= 1
            j -= 1
        r = ""
        #print(res)
        for x in res:
            r = r + str(x)
        if c == 1:
            r = '1' + r
        return r
        