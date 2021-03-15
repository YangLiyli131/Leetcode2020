class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        hp = []
        for x in classes:
            a,b = x[0],x[1]
            d = -a/float(b) + (a+1)/float(b+1)
            heapq.heappush(hp, [-d, a, b])
        while extraStudents != 0:
            pre = heapq.heappop(hp)
            a,b = pre[1]+1, pre[2]+1
            d = -a/float(b) + (a+1)/float(b+1)
            heapq.heappush(hp, [-d, a, b])
            extraStudents -= 1 
        r = 0
        while hp:
            x = heapq.heappop(hp)
            r += x[1] / float(x[2])
        return r / float(len(classes))