class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dict = {}
        for x in list(s):
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        max_odd = 0
        flag = False
        for k in dict:
            if dict[k] % 2 == 0:
                res += dict[k]
            else:
                flag = True
                res += dict[k]-1
        if flag: res += 1
        return res
        