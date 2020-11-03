class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.q.append(timestamp)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        thresh = timestamp - 300
        while self.q:
            if self.q[0] <= thresh:
                self.q.pop(0)
            else:
                break
        return len(self.q)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)



class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = [[0,i+1] for i in range(300)]

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        idx = int((timestamp - 1) % 300)
        if self.counter[idx][1] == timestamp:
            self.counter[idx][0] += 1
        else:
            self.counter[idx][1] = timestamp
            self.counter[idx][0] = 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        for x in self.counter:
            t = x[1]
            if timestamp - t < 300:
                res += x[0]
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)