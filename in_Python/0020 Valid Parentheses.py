class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in list(s):
            if x in ['[','{','(']:
                stack.append(x)
            else:
                if x == ']' and len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                elif x == ')' and len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                elif x == '}' and len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        