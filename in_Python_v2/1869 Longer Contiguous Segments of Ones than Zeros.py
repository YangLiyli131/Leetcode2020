class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if '1' not in s:
            return False
        if '0' not in s:
            return True
        a1 = s.split('0')
        m1 = 0
        for x in a1:
            m1 = max(m1, len(x))
        a2 = s.split('1')
        m2 = 0
        for x in a2:
            m2 = max(m2, len(x))
        return m1 > m2