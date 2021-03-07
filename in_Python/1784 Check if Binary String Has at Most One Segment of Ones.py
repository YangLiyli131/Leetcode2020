class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        firstz = 0
        for i in range(len(s)):
            if s[i] == '0':
                firstz = i
                break
        if firstz == 0:
            return True
        for i in range(firstz+1, len(s)):
            if s[i] == '1':
                return False
        return True