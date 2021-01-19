class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """        
        def check(x,y):
            return x[0] == y[0] and x[1] == y[1]
        
        visited = {}
        q = collections.deque()
        q.append((start[0], start[1], 0))
        visited[(start[0], start[1])] = 0
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                x = q.popleft()
                i,j,L = x[0],x[1],x[2]
                while i >= 0 and maze[i][j] != 1:
                    i -= 1
                d = L + abs(x[0] - i) - 1
                r1 = (i+1, j, d)
                if (i+1,j) in visited:
                    if d < visited[(i+1,j)]:
                        visited[(i+1,j)] = d     
                        q.append(r1)
                else:                         
                    visited[(i+1,j)] = d
                    q.append(r1)
                                    
                i,j,L = x[0],x[1],x[2]
                while i < len(maze) and maze[i][j] != 1:
                    i += 1
                d = L + abs(x[0] - i) - 1
                r2 = (i-1, j, d)
                if (i-1,j) in visited:
                    if d < visited[(i-1,j)]:
                        visited[(i-1,j)] = d     
                        q.append(r2)
                else:                         
                    visited[(i-1,j)] = d
                    q.append(r2)
                
                i,j,L = x[0],x[1],x[2]
                while j >= 0 and maze[i][j] != 1:
                    j -= 1
                d = L + abs(x[1] - j) - 1
                r3 = (i, j+1, d)
                if (i,j+1) in visited:
                    if d < visited[(i,j+1)]:
                        visited[(i,j+1)] = d     
                        q.append(r3)
                else:                         
                    visited[(i,j+1)] = d
                    q.append(r3)
                
                i,j,L = x[0],x[1],x[2]
                while j < len(maze[0]) and maze[i][j] != 1:
                    j += 1
                d = L + abs(x[1] - j) - 1
                r4 = (i, j-1, d)
                if (i,j-1) in visited:
                    if d < visited[(i,j-1)]:
                        visited[(i,j-1)] = d     
                        q.append(r4)
                else:                         
                    visited[(i,j-1)] = d
                    q.append(r4)
        if (destination[0], destination[1]) not in visited:
            return -1
        return visited[(destination[0], destination[1])]