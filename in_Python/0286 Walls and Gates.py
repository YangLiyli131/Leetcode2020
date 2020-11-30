class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if rooms == None or len(rooms) == 0 or len(rooms[0]) == 0:
            return rooms
        locs = []
        row = len(rooms)
        col = len(rooms[0])
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    locs.append([i,j])
        while locs:
            zero = locs.pop(0)
            i = zero[0]
            j = zero[1]
            q = collections.deque([(i+1,j,1), (i-1,j,1), (i,j+1,1), (i,j-1,1)])
            while q:
                x,y,val = q.popleft()
                if 0 <= x < row and 0 <= y < col and rooms[x][y] > val:
                    rooms[x][y] = val
                    q.extend([(x+1,y,val+1), (x-1,y,val+1), (x,y+1,val+1), (x,y-1,val+1)])
        
                    