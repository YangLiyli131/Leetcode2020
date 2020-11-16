class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obs = set()
        for x in obstacles:
            obs.add(tuple(x))
        dirt = 'u'
        d1 = {'u':'r','l':'u','d':'l','r':'d'}
        d2 = {'u':'l','l':'d','d':'r','r':'u'}
        loc = [0,0]
        res = 0
        for cm in commands:
            if cm == -1:
                dirt = d1[dirt]
            elif cm == -2:
                dirt = d2[dirt]
            else:
                steps = cm
                while steps != 0:
                    if dirt == 'u':
                        nexloc = [loc[0], loc[1]+1]
                    elif dirt == 'd':
                        nexloc = [loc[0], loc[1]-1]
                    elif dirt == 'l':
                        nexloc = [loc[0]-1, loc[1]]
                    else:
                        nexloc = [loc[0]+1, loc[1]]
                    if tuple(nexloc) in obs:
                        break
                    steps -= 1
                    loc = nexloc
                    res = max(res, loc[0] **2 + loc[1] **2)
        return res
                
        