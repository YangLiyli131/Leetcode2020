class TweetCounts(object):

    def __init__(self):
        self.d = {}

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        if tweetName in self.d:
            self.d[tweetName].append(time)
        else:
            self.d[tweetName] = [time]

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        if freq == 'minute':
            s = 60
        elif freq == 'hour':
            s = 3600
        else:
            s = 3600 * 24
        r = [0] * ((endTime - startTime) // s + 1)
        for t in self.d[tweetName]:
            if t < startTime or t > endTime:
                continue
            c = (t - startTime) // s 
            r[c] += 1
        return r


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)