class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        d = {}
        for x in regions:
            for i in range(1, len(x)):
                cur = x[i]
                if cur not in d:
                    d[cur] = x[0]
        q = collections.deque()
        q.append(region1)
        l1 = []
        while q:
            r = q.popleft()
            l1.append(r)
            if r in d:
                q.append(d[r])
        q = collections.deque()
        q.append(region2)
        l2 = []
        while q:
            r = q.popleft()
            l2.append(r)
            if r in d:
                q.append(d[r])
        for x in l1:
            if x in l2:
                return x
        return None