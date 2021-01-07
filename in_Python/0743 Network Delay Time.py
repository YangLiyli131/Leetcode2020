class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        A = {}
        for x in times:
            a = x[0]
            b = x[1]
            c = x[2]
            if a not in A:
                A[a] = [[b,c]]
            else:
                A[a].append([b,c])
        timestaken = [sys.maxint] * N
        q = collections.deque()
        q.append([0,K])
        while q:
            time, node = q.popleft()
            if time < timestaken[node-1]:
                timestaken[node-1] = time
                if node in A:
                    for nex in A[node]:
                        q.append([nex[1] + time, nex[0]])
        res = max(timestaken)
        if res == sys.maxint:
            return -1
        return res
        
        