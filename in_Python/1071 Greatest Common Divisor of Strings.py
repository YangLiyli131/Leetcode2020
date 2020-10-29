class Solution(object):
    def check(self, s, pre):
        l = len(pre)
        L = len(s)
        if L % l != 0:
            return False
        j = l
        while j <= L:
            cur = s[(j-l) : j]
            if cur != pre:
                return False
            j += l
        return True
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        s1 = ''
        s2 = ''
        if len(str1) >= len(str2):
            s1 = str1
            s2 = str2
        else:
            s1 = str2
            s2 = str1
        j = len(s2)
        while j > 0:
            prex = s2[0:j]
            if self.check(s1, prex) and self.check(s2, prex):
                return prex
            j -= 1
        return ''