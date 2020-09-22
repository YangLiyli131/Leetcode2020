class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        e = []
        i = 0
        j = 0
        e.append([i,j])
        for p in path:
            if p == 'N':
                j += 1
            elif p == 'W':
                i -= 1
            elif p == 'S':
                j -= 1
            else:
                i += 1
            cur = [i,j]
            if cur in e:
                return True
            e.append(cur)
        return False