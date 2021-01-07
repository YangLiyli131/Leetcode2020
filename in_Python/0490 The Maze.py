class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        def check(a, b):
            return a[0] == b[0] and a[1] == b[1]
        visited = set()
        visited.add((start[0], start[1]))
        q = collections.deque()
        q.append(start)
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.popleft()
                i,j = h[0], h[1]      
                while i >= 0 and maze[i][j] != 1:
                    i -= 1
                r1 = (i+1,j)
                if r1 not in visited:
                    visited.add(r1)
                    q.append(list(r1))
                    if check(r1, destination):
                        return True
                i,j = h[0], h[1]
                while i < len(maze) and maze[i][j] != 1:
                    i += 1
                r2 = (i-1, j)
                if r2 not in visited:
                    visited.add(r2)
                    q.append(list(r2))
                    if check(r2, destination):
                        return True
                i,j = h[0], h[1]
                while j >= 0 and maze[i][j] != 1:
                    j -= 1
                r3 = (i, j+1)
                if r3 not in visited:
                    visited.add(r3)
                    q.append(list(r3))
                    if check(r3, destination):
                        return True
                i,j = h[0], h[1]
                while j < len(maze[0]) and maze[i][j] != 1:
                    j += 1
                r4 = (i, j-1)
                if r4 not in visited:
                    visited.add(r4)
                    q.append(list(r4))
                    if check(r4, destination):
                        return True
        return False
                    