class Solution(object):
    def isleap(self, y):
        return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        d1 = date1.split('-')
        d2 = date2.split('-')
        days1, days2 = 0,0
        y1 = int(d1[0])
        y2 = int(d2[0])
        m1 = int(d1[1])
        m2 = int(d2[1])
        z1 = int(d1[2])
        z2 = int(d2[2])
        for i in range(1971, y1):
            if self.isleap(i):
                days1 += 366
            else:
                days1 += 365
        for i in range(1971, y2):
            if self.isleap(i):
                days2 += 366
            else:
                days2 += 365
        odd = [1,3,5,7,8,10,12]
        even = [4,6,9,11]
        for i in range(m1):
            if i in odd:
                days1 += 31
            elif i in even:
                days1 += 30
            elif i == 2:
                if self.isleap(y1):
                    days1 += 29
                else:
                    days1 += 28
        for i in range(m2):
            if i in odd:
                days2 += 31
            elif i in even:
                days2 += 30
            elif i == 2:
                if self.isleap(y2):
                    days2 += 29
                else:
                    days2 += 28
        days1 += z1
        days2 += z2
        return abs(days1 - days2)