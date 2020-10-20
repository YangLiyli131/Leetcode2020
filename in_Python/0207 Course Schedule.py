class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        coursemap = {}
        degree = [0] * numCourses
        for i in range(numCourses):
            coursemap[i] = []
        for p in prerequisites:
            t = p[0]
            s = p[1]
            coursemap[s].append(t)
            degree[t] += 1
        res = []
        q = []
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        for i in q:
            for j in coursemap[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    q.append(j)
        return len(q) == numCourses
        
        
        