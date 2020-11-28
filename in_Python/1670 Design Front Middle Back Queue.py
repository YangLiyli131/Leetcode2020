class FrontMiddleBackQueue(object):

    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.q1.appendleft(val)
        if len(self.q1) > len(self.q2):
            self.q2.appendleft(self.q1.pop())

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.q1) == len(self.q2):
            self.q2.appendleft(val)
        else:
            self.q1.append(val)

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.q2) > len(self.q1):
            self.q1.append(self.q2.popleft())
        self.q2.append(val)

    def popFront(self):
        """
        :rtype: int
        """
        if len(self.q1) < len(self.q2):
            self.q1.append(self.q2.popleft())
        if self.q1:
            return self.q1.popleft()
        else:
            return -1

    def popMiddle(self):
        """
        :rtype: int
        """
        if len(self.q1) == len(self.q2):
            if self.q1:
                return self.q1.pop()
            else:
                return -1
        else:
            return self.q2.popleft()

    def popBack(self):
        """
        :rtype: int
        """
        if len(self.q1) == len(self.q2):
            if not self.q1:
                return -1
            self.q2.appendleft(self.q1.pop())
        return self.q2.pop()
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()