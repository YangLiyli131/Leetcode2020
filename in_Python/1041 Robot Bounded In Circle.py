class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dl = {'n':'w','w':'s','s':'e','e':'n'}
        dr = {'n':'e','e':'s','s':'w','w':'n'}
        dire = 'n'
        i,j = 0,0
        for x in instructions:
            if x == 'G':
                if dire == 'n':
                    j += 1
                elif dire == 'e':
                    i += 1
                elif dire == 's':
                    j -= 1
                else:
                    i -= 1
            elif x == 'L':
                dire = dl[dire]
            else:
                dire = dr[dire]
        if i == 0 and j == 0:
            return True
        if dire != 'n':
            return True
        return False