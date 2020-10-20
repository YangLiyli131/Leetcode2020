class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        coursemap = {}
        for i in range(numCourses):
            coursemap[i] = []
        degree = [0] * numCourses
        for p in prerequisites:
            preq = p[1]
            tar = p[0]
            degree[tar] += 1
            coursemap[preq].append(tar)
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for i in bfs:
            for j in coursemap[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        if len(bfs) != numCourses:
            return []
        return bfs
        