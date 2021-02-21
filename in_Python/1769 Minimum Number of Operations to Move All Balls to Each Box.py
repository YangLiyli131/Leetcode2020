class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        idx = []
        for i,j in enumerate(boxes):
            if j == '1':
                idx.append(i)
        r = []
        for i in range(len(boxes)):
            s = 0
            for x in idx:
                s += abs(x-i)
            r.append(s)
        return r