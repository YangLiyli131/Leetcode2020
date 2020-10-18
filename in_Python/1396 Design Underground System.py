class UndergroundSystem(object):

    def __init__(self):
        self.checkin = {}
        self.edges = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkin[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        last = self.checkin[id]
        source = last[0]
        tt = t - last[1]
        if (source, stationName) not in self.edges:
            self.edges[(source, stationName)] = [tt]
        else:
            self.edges[(source, stationName)].append(tt)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        x = self.edges[startStation, endStation]
        return sum(x) / float(len(x))


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)