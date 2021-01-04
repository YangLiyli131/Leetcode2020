class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        row = len(heightMap)
        col = len(heightMap[0])
        hp = []
        seen = []
        res = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(row):
            seen.append([0] * col)
        for i in range(row):
            heapq.heappush(hp, [heightMap[i][0], i, 0])
            heapq.heappush(hp, [heightMap[i][col-1], i, col-1])
            seen[i][0] = 1
            seen[i][col-1] = 1
        for j in range(col):
            heapq.heappush(hp, [heightMap[0][j], 0, j])
            heapq.heappush(hp, [heightMap[row-1][j], row-1, j])
            seen[0][j] = seen[row-1][j] = 1
        while hp:
            [h, a, b] = heapq.heappop(hp)
            for d in directions:
                nexta, nextb = a + d[0], b + d[1]
                if nexta < 0 or nextb < 0 or nexta >= row or nextb >= col or seen[nexta][nextb] == 1:
                    continue
                seen[nexta][nextb] = 1
                res += max(0, h - heightMap[nexta][nextb])
                heapq.heappush(hp, [max(h, heightMap[nexta][nextb]), nexta, nextb])
        return res