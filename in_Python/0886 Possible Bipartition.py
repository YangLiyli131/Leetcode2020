class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if N < 2:
            return True
        color = [-1] * N
        d = {}
        for i in range(N):
            d[i] = []
        for p in dislikes:
            a = p[0]-1
            b = p[1]-1
            d[a].append(b)
            d[b].append(a)
        for i in range(N):
            if color[i] != -1:
                continue
            color[i] = 1
            q = [i]
            while q:
                h = q.pop(0)
                for x in d[h]:
                    if color[x] == -1:
                        color[x] = 1 - color[h]
                        q.append(x)
                    elif color[x] == color[h]:
                        return False
        return True