class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        n = num
        flag = False
        t = []
        while num != 0:
            t.insert(0,num % 10)
            num /= 10
        for i in range(len(t)):
            if t[i] == 6:
                t[i] = 9
                flag = True
                break
        if not flag: return n
        res = 0
        p = len(t)-1
        for i in t:
            res += i * (10 ** p)
            p -= 1
        return res
        