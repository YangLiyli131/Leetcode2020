class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        num_xy = 0
        num_yx = 0
        for i in range(len(s1)):
            a = s1[i]
            b = s2[i]
            if a == b:
                continue
            if a == 'x' and b == 'y':
                num_xy += 1
            else:
                num_yx += 1
        res = 0
        if (num_xy + num_yx) % 2 != 0:
            return -1
        res += num_xy / 2 + num_yx / 2
        if num_xy % 2 == 1:
            res += 2
        return res