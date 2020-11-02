class Solution(object):
    def trans(self, time):
        hour = time[0:2]
        minu = time[3:5]
        h = 0
        m = 0
        if hour == '00':
            h = 0
        elif hour[0] == '0':
            h = int(hour[1])
        else:
            h = int(hour)
        if minu == '00':
            m = 0
        elif minu[0] == '0':
            m = int(minu[1])
        else:
            m = int(minu)
        return 60 * h + m
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        total = 24 * 60
        arr = []
        for t in timePoints:
            arr.append(self.trans(t))
        res = total
        arr.sort()
        arr.append(arr[0])
        for i in range(1, len(arr)):
            dif = abs(arr[i] - arr[i-1])
            dif = min(dif, total - dif)
            res = min(res, dif)
        
        return res