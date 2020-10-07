class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.d:
            t = []
            t.append([value, timestamp])
            self.d[key] = t
        else:
            t = self.d[key]
            t.append([value, timestamp])
            self.d[key] = t   

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.d:
            return ""
        values = self.d[key]
        i, j = 0, len(values)
        while i < j:
            m = i + (j-i) / 2
            if values[m][1] <= timestamp:
                i = m + 1
            else:
                j = m
        if j == 0:
            return ""
        else:
            return values[j-1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)