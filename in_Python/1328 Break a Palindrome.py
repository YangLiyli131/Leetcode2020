class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        def check(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        if len(palindrome) == 1:
            return ''
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                tmp = palindrome[:i] + 'a' + palindrome[i+1:]
                if not check(tmp):
                    return tmp
        return palindrome[: len(palindrome)-1] + 'b'