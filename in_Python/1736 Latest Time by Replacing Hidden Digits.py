class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        res = []
        hour = time[0:2]
        minu = time[3:5]
        if hour == '??':
            res.append('23')
        elif hour[0] == '?':
            if hour[1] < '4':
                res.append('2' + hour[1])
            else:
                res.append('1' + hour[1])
        elif hour[1] == '?':
            if hour[0] == '2':
                res.append('23')
            else:
                res.append(hour[0] + '9')
        else:
            res.append(hour)
        res.append(':')
        
        if minu == '??':
            res.append('59')
        elif minu[0] == '?':
            res.append('5' + minu[1])
        elif minu[1] == '?':
            res.append(minu[0] + '9')
        else:
            res.append(minu)
        return ''.join(res)
            
        