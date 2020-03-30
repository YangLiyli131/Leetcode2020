class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        #return str.lower()
        res = ''
        up = ord('Z')
        low = ord('A')
        m = ord('z')
        for c in str:
            x = ord(c)
            if low <= x <= up:
                res += chr(x - up + m)
            else:
                res += c
        return res