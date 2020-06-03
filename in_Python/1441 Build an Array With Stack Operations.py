class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res = []
        idx = 0
        for i in range(1,n+1):
            if idx == len(target):
                break
            if i == target[idx]:
                res.append("Push")
                idx += 1
            else:
                res.append("Push")
                res.append("Pop")
        return res