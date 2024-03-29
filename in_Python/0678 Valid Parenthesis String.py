class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            elif i == ')':
                cmax -= 1
                cmin = max(cmin-1, 0)
            else:
                cmax += 1
                cmin = max(cmin-1, 0)
            if cmax < 0:
                return False
        return cmin == 0