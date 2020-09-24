class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if trust == None or len(trust) == 0:
            if N == 1:
                return N
            else:
                return -1
        indeg = []
        outdeg = []
        for i in range(N+1):
            indeg.append(0)
            outdeg.append(0)
        for t in trust:
            a = t[0]
            b = t[1]
            outdeg[a] += 1
            indeg[b] += 1
        #print(indeg)
        #print(outdeg)
        for i in range(N+1):
            if outdeg[i] == 0 and indeg[i] == N-1:
                return i
        return -1
            
        