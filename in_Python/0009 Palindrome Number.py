class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        t = []
        while x != 0:
            t.append(x % 10)
            x /= 10
        i, j = 0, len(t)-1
        while i < j:
            if t[i] != t[j]:
                return False
            i += 1
            j -= 1
        return True
        