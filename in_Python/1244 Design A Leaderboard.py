class Leaderboard(object):

    def __init__(self):
        self.board = {}

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if playerId not in self.board:
            self.board[playerId] = score
        else:
            self.board[playerId] += score

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        res = 0
        v = []
        for x in self.board.values():
            v.append(-x)
        heapq.heapify(v)
        while K != 0:
            res -= heapq.heappop(v)
            K -= 1
        return res

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        self.board[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)