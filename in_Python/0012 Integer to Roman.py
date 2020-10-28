class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {}
        d[1] = "I"
        d[5] = "V"
        d[10] = "X"
        d[50] = "L"
        d[100] = "C"
        d[500] = "D"
        d[1000] = "M"
        d[4] = "IV"
        d[9] = "IX"
        d[40] = "XL"
        d[90] = "XC"
        d[400] = "CD"
        d[900] = "CM"
        res = []
        ks = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        while num != 0:
            for k in ks:
                if k <= num:
                    res.append(d[k]) 
                    num -= k
                    break
        return ''.join(res)
                