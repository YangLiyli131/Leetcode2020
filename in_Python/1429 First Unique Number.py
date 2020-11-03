class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.q = collections.deque(nums)
        self.c = collections.Counter(nums)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        while self.q:
            x = self.q.popleft()
            if self.c[x] == 1:
                self.q.appendleft(x)
                return x
        return -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.q.append(value)
        self.c[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)