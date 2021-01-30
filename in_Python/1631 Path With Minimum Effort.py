class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        row, col = len(heights), len(heights[0])
        mh = [(0,0,0)]
        dist = [[sys.maxint] * col for _ in range(row)]
        dirt = [0,1,0,-1,0]
        while mh:
            d,r,c = heapq.heappop(mh)
            if d > dist[r][c]:
                continue
            if r == row-1 and c == col-1:
                return d
            for i in range(4):
                nextr, nextc = r + dirt[i], c + dirt[i+1]
                if 0 <= nextr < row and 0 <= nextc < col:
                    newd = max(d, abs(heights[nextr][nextc] - heights[r][c]))
                    if newd < dist[nextr][nextc]:
                        dist[nextr][nextc] = newd
                        heapq.heappush(mh, (newd, nextr, nextc))
        return -1