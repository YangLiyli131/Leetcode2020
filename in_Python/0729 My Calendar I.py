class MyCalendar(object):

    def __init__(self):
        self.arr = []
    
    def overlap(self, a, b):
        return a[0] < b[1] and b[0] < a[1]
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        cur = [start, end]
        if len(self.arr) == 0:
            self.arr.append(cur)
            return True
        else:
            for x in self.arr:
                if self.overlap(x, cur):
                    return False
            self.arr.append(cur)
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)