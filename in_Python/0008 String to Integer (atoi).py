class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        intMax = 2147483647
        intMin = -2147483648
        str = str.strip()
        if not str:
            return 0
        sign = 1
        i = 0
        if str[i] == '+':
            sign = 1
            i += 1
        elif str[i] == '-':
            sign = -1
            i += 1
        res = 0
        while i < len(str):
            if not str[i].isdigit():
                break
            res = res * 10 + (ord(str[i]) - ord('0'))
            if res > intMax:
                break
            i += 1
        res = sign * res
        if res < intMin:
            return intMin
        elif res > intMax:
            return intMax
        else:
            return res