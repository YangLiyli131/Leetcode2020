class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        level = 2
        r = ['(','1',',','2',')']
        while pow(2,level) <= n:
            up = pow(2, level) + 1
            level += 1
            nr = []
            for x in r:
                if x in ['(',')',',']:
                    nr.append(x)
                else:
                    nr.append('(')
                    nr.append(x)
                    nr.append(',')
                    nr.append(str(up - int(x)))
                    nr.append(')')
            r = nr
        return ''.join(r)
            
            