class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        row = len(forest)
        col = len(forest[0])
        d = {}
        for i in range(row):
            for j in range(col):
                cur = forest[i][j]
                if cur != 0:
                    d[cur] = [i,j]
                
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def helper(graph, i,j, a,b):
            level = 0
            if i == a and j == b:
                return 0
            q = collections.deque()
            q.append([i,j])
            seen = set()
            seen.add((i,j))
            while q:
                n = len(q)
                level += 1
                while n != 0:
                    n -= 1
                    thisi, thisj = q.popleft()
                    for d in directions:
                        nexti, nextj = thisi + d[0], thisj + d[1]
                        if nexti == a and nextj == b:
                            return level
                        if 0 <= nexti < len(graph) and 0 <= nextj < len(graph[0]) and (nexti,nextj) not in seen and graph[nexti][nextj] != 0:
                            seen.add((nexti,nextj))
                            q.append([nexti,nextj])
            return -1
                    
        
        res = 0
        heights = d.keys()
        heights.sort()
        cur = [0,0]
        for h in heights:
            nex = d[h]
            x = helper(forest, cur[0], cur[1], nex[0], nex[1])
            if x == -1:
                return -1
            res += x
            cur = nex
        return res