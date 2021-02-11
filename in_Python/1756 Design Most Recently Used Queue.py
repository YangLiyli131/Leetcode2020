class MRUQueue(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.dq = collections.deque()
        for i in range(1,n+1):
            self.dq.append(i)
        self.t = collections.deque()

    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k == len(self.dq):
            return self.dq[-1]
        while k != 0:
            k -= 1
            self.t.append(self.dq.popleft())
        r = self.t[-1]
        self.dq.append(self.t.pop())
        while self.t:
            self.dq.appendleft(self.t.pop())
        return r


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)