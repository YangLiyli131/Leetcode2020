class FileSharing(object):

    def __init__(self, m):
        """
        :type m: int
        """
        self.d = collections.defaultdict(set)
        self.u = collections.defaultdict(set)
        self.pool = []

    def join(self, ownedChunks):
        """
        :type ownedChunks: List[int]
        :rtype: int
        """
        idx = len(self.u) + 1
        if self.pool:
            idx = heapq.heappop(self.pool)
        self.u[idx] = set(ownedChunks)
        for x in ownedChunks:
            self.d[x].add(idx)
        return idx
        
    def leave(self, userID):
        """
        :type userID: int
        :rtype: None
        """
        if userID not in self.u:
            return
        for c in self.u[userID]:
            self.d[c].remove(userID)
        self.u[userID] = set()
        heapq.heappush(self.pool, userID)

    def request(self, userID, chunkID):
        """
        :type userID: int
        :type chunkID: int
        :rtype: List[int]
        """
        
        r = list(self.d[chunkID])
        r.sort()
        if len(r) != 0:
            self.d[chunkID].add(userID)
            self.u[userID].add(chunkID)
        return r


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)