class LogSystem(object):

    def __init__(self):
        self.log = {}

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        self.log[id] = timestamp.split(':')

    def retrieve(self, start, end, granularity):
        """
        :type start: str
        :type end: str
        :type granularity: str
        :rtype: List[int]
        """
        sl = start.split(':')
        el = end.split(':')
        di = {'Year':0,'Month':1, 'Day':2, 'Hour':3, 'Minute':4, 'Second':5}
        rag = di[granularity]
        begin = ''.join(sl[:rag+1])
        last = ''.join(el[:rag+1])
        res = []
        for k in self.log:
            cur = self.log[k]
            current = ''.join(cur[:rag+1])
            if begin <= current <= last:
                res.append(k)
        return res

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)