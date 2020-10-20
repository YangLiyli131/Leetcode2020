class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        N = len(tasks)
        d = {}
        for i in tasks:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        maxcount = 0
        for k in d:
            if d[k] > maxcount:
                maxcount = d[k]
        maxtask = []
        for k in d:
            if d[k] == maxcount:
                maxtask.append(k)
        L = len(maxtask)
        le = (n+1) * (maxcount-1) + L
        return max(N,le)
        
        
        