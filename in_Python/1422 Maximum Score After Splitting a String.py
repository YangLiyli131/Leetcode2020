class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_zero = []
        num_ones = []
        if s[0] == '0':
            num_zero.append(1)
        else:
            num_zero.append(0)
        if s[-1] == '1':
            num_ones.append(1)
        else:
            num_ones.append(0)
        for i in range(1,len(s)):
            if s[i] == '0':
                num_zero.append(num_zero[-1] + 1)
            else:
                num_zero.append(num_zero[-1])
        for i in range(len(s)-2, -1, -1):
            if s[i] == '1':
                num_ones.append(num_ones[-1] + 1)
            else:
                num_ones.append(num_ones[-1])
        t = []
        for i in num_ones:
            t.insert(0,i)
        res = 0
        for i in range(len(num_zero)):
            if i + 1 < len(t):
                res = max(res, num_zero[i] + t[i+1])
        return res
        