class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        res = 0
        for i in range(len(moves)):
            if moves[i] == 'U':
                res += 1
            elif moves[i] == 'D':
                res -= 1
            elif moves[i] == 'L':
                res += 2
            else:
                res -= 2
        return res == 0
        
        