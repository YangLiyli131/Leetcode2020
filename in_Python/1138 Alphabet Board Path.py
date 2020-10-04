class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        st = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        idx = 0
        for i in range(5):
            for j in range(5):
                d[st[idx]] = [i,j]
                idx += 1
        d['z'] = [5,0]
        #print(d)
        res = ''
        t = target[0]
        co = d[t]
        x = co[0]
        y = co[1]
        pre = target[0]
        prex = co[0]
        prey = co[1]
        while x != 0:
            res += 'D'
            x -= 1
        while y != 0:
            res += 'R'
            y -= 1
        res += '!'
        for i in range(1, len(target)):
            letter = target[i]
            co = d[letter]
            x = co[0]
            y = co[1]
            if pre == 'z' and letter != 'z':
                res += 'U'
                prex -= 1
            dx = x - prex
            dy = y - prey
            if dy > 0:
                while dy != 0:
                    res += 'R'
                    dy -= 1
            else:
                while dy != 0:
                    res += 'L'
                    dy += 1
            if dx > 0:
                while dx != 0:
                    res += 'D'
                    dx -= 1 
            else:
                while dx != 0:
                    res += 'U'
                    dx += 1
            res += '!'
            prex = co[0]
            prey = co[1]
            pre = letter
        return res
            
            