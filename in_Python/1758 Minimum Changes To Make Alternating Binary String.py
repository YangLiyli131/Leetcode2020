class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        oddz, oddo, evenz, eveno = 0,0,0,0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    eveno += 1
                else:
                    evenz += 1
            else:
                if s[i] == '1':
                    oddo += 1
                else:
                    oddz += 1

        return min(oddo+evenz, eveno+oddz)