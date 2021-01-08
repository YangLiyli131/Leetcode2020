class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        d = {}
        day = 0
        while tuple(cells) not in d and N != 0:
            d[tuple(cells)] = day
            day += 1
            cur = [0]
            N -= 1
            for i in range(1, len(cells)-1):
                if cells[i-1] + cells[i+1] == 2 or cells[i-1] + cells[i+1] == 0:
                    cur.append(1)
                else:
                    cur.append(0)
            cur.append(0)
            cells = cur
        if N == 0:
            return cells
        curday = d[tuple(cells)]
        period = day - curday
        lastday = curday + N % period
        for x in d:
            if d[x] == lastday:
                return list(x)
        return None
        