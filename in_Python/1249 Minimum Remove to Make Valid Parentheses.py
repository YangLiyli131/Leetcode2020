class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = ''
        left = 0
        right = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                right += 1
        curleft, curright = 0, 0        
        for x in s:
            m = min(left, right)
            if x == ')' and curright >= curleft:
                right -= 1
                continue
            elif x == '(' and curleft >= m:
                left -= 1
                continue
            else:
                st += x
                if x == '(':
                    curleft += 1
                if x == ')':
                    curright += 1
                
        return st
            