class Solution(object):
    def isLeap(self,y):
        if y % 400 == 0:
            return 1
        if y % 4 == 0 and y % 100 != 0:
            return 1
        return 0
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        dayNames = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def days(d, m, yy):
            res = 0
            for y in range(yy-1, 1970, -1):
                res += 365 + self.isLeap(y)
            res += sum(daysInMonth[:m - 1])
            res += d
            if m > 2:
                res += self.isLeap(yy)
            return res
        today = days(3, 10, 2020)
        ds = days(day, month, year)
        dfi = ds - today
        return dayNames[dfi % 7]