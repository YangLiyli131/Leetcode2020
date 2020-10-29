class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.stacks = []
        self.cap = capacity
        self.open_positions = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        while self.open_positions and self.open_positions[0] < len(self.stacks) and len(self.stacks[self.open_positions[0]]) == self.cap:
            heapq.heappop(self.open_positions)
        if not self.open_positions:
            heapq.heappush(self.open_positions, len(self.stacks))
        if self.open_positions[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.open_positions[0]].append(val)
        
    def pop(self):
        """
        :rtype: int
        """
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.popAtStack(len(self.stacks)-1)

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.open_positions, index)
            return self.stacks[index].pop()
        return -1
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)