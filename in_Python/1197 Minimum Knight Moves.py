class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == 0 and y == 0:
            return 0
        seen = set()
        seen.add((0,0))
        q = collections.deque()
        q.append((0,0))
        di = [[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]
        r = 0
        while q:
            n = len(q)
            r += 1
            while n != 0:
                n -= 1
                curx, cury = q.popleft()
                for d in di:
                    nex, ney = curx + d[0], cury + d[1]
                    if nex == x and ney == y:
                        return r
                    if (nex,ney) not in seen:
                        seen.add((nex,ney))
                        q.append((nex,ney))
        return -1