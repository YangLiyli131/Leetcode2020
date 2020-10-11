class Solution(object):
    def check(self, y):
        y = int(y)
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            return True
        return False
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        y,m,d = date.split('-')
        if self.check(y):
            days[1] += 1
        month = int(m)
        res = int(d)
        for i in range(month-1):
            res += days[i]
        return res
        
        