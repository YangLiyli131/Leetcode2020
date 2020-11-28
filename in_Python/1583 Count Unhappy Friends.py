class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        mat = []
        for i in range(n):
            mat.append([0] * n)
        for i in range(len(preferences)):
            cur = preferences[i]
            for j in range(n-1):
                mat[i][cur[j]] = n-1-j
        res = set()
        for p in pairs:
            x = p[0]
            y = p[1]
            for q in pairs:
                u = q[0]
                v = q[1]
                if x == u and y == v:
                    continue
                if mat[x][u] > mat[x][y] and mat[u][x] > mat[u][v]:
                    res.add(x)
                if mat[x][v] > mat[x][y] and mat[v][x] > mat[v][u]:
                    res.add(x)
                if mat[y][v] > mat[y][x] and mat[v][y] > mat[v][u]:
                    res.add(y)
                if mat[y][u] > mat[y][x] and mat[u][y] > mat[u][v]:
                    res.add(y)
        return len(res)
                