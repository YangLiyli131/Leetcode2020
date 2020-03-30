class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n % 2 == 1:
            return 'b' * n
        else:
            return 'a' * (n-1) + 'b'