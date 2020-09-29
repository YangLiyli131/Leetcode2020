class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        visited = []
        q = []
        q.append(0)
        visited.append(0)
        while len(q) != 0:
            root = q.pop(0)
            nextnodes = rooms[root]
            for ni in nextnodes:
                if ni in visited:
                    continue
                else:
                    visited.append(ni)
                    q.append(ni)
        return len(visited) == N