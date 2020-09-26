class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        d = date.split(' ')
        day = d[0]
        day = day[0:len(day)-2]
        if len(day) == 1:
            day = '0' + day
        year = d[-1]
        m = d[1]
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        m = month.index(m)+1
        m = str(m)
        if len(m) == 1:
            m = '0' + m
        return year + '-' + m + '-' + day