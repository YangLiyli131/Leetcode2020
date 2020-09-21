class RecentCounter(object):
    
    def __init__(self):
        self.dq = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.dq.append(t)
        while self.dq[0] < t - 3000:
            self.dq.popleft()  
        return len(self.dq)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)