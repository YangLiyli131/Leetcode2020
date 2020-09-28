class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        visited = []
        visited.append([sr,sc])
        toChange = []
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while len(visited) != 0:
            head = visited.pop(0)
            curi = head[0]
            curj = head[1]
            toChange.append(head)
            for d in directions:
                nexti = curi + d[0]
                nextj = curj + d[1]
                if 0 <= nexti < len(image) and 0 <= nextj < len(image[0]) and [nexti, nextj] not in toChange:
                    if image[nexti][nextj] == image[curi][curj]:
                        visited.append([nexti,nextj])
        for x in toChange:
            image[x[0]][x[1]] = newColor
        return image
            