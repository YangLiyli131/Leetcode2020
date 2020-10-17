class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.alltweets = []
        self.following = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.alltweets.append([userId, tweetId])
        if userId not in self.following:
            self.following[userId] = [userId]
        else:
            t = self.following[userId]
            if userId not in t:
                t.append(userId)
                self.following[userId] = t

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res = []
        if userId not in self.following:
            return res
        f = self.following[userId]
        total = 0
        for i in range(len(self.alltweets)-1, -1, -1):
            x = self.alltweets[i]
            if x[0] in f:
                res.append(x[1])
                total += 1
            if total == 10:
                break
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.following:
            self.following[followerId] = []
        t = self.following[followerId]
        if followeeId not in t:
            t.append(followeeId)
            self.following[followerId] = t

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.following:
            t = self.following[followerId]
            if followeeId != followerId and followeeId in t:
                t.remove(followeeId)
                self.following[followerId] = t        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)