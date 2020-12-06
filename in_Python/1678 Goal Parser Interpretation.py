class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = []
        i = 0
        while i < len(command):
            cur = command[i]
            if cur == 'G':
                res.append(cur)
                i += 1
            elif cur == '(':
                if command[i+1] == ')':
                    res.append('o')
                    i += 2
                else:
                    res.append('al')
                    i += 4
        return ''.join(res)