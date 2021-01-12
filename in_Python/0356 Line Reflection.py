class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        d = {}
        for p in points:
            x = p[0]
            y = p[1]
            if y not in d:
                d[y] = [x]
            else:
                if x not in d[y]:
                    d[y].append(x)
        middle = None
        for y in d:
            row = d[y]
            row.sort()
            mm = row[0] + row[-1]
            if middle == None:
                middle = mm
            else:
                if middle != mm:
                    return False
            i,j = 0, len(row)-1
            if len(row) == 1 and 2 * row[0] == middle:
                continue
            while i < j:
                if row[i] + row[j] != middle:
                    return False
                i += 1
                j -= 1
            if i == j:
                if 2 * row[i] != middle:
                    return False
        return True
        