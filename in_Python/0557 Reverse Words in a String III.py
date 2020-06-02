class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = s.split(' ')
        st = ""
        for ss in ls:
            st += ss[::-1] + ' '
        return st[0:len(st)-1]
        