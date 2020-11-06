class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        s = 1
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                s += i
                if i != num / i:
                    s += num / i
        return s == num