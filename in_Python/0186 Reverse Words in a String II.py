class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i,j = 0, len(s)-1
        while i < j:
            cur = s[i]
            s[i] = s[j]
            s[j] = cur
            i += 1
            j -= 1
        i,j = 0,0
        while j < len(s):
            while j < len(s) and s[j] != ' ':
                j += 1
            right = j-1
            while i < right:
                cur = s[i]
                s[i] = s[right]
                s[right] = cur
                i += 1
                right -= 1
            i = j + 1
            j = i
        