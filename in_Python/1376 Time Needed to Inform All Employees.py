class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        self.res = 0
        hm = collections.defaultdict(list)
        for i, m in enumerate(manager):
            hm[m].append(i)
        def dfs(i,t):
            self.res = max(self.res,t)
            for x in hm[i]:
                dfs(x,t + informTime[i])
        dfs(headID,0)
        return self.res