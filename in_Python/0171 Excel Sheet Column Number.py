class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        power = 0
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            n = ord(c) - ord('A') + 1
            res += n * pow(26, power)
            power += 1
        return res