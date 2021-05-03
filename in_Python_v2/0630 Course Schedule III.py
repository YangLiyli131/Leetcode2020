class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses = sorted(courses, key = lambda x: x[1])
        hq = []
        t = 0
        for c in courses:
            if t + c[0] <= c[1]:
                heapq.heappush(hq, -c[0])
                t += c[0]
            elif len(hq) != 0 and -hq[0] > c[0]:
                t += c[0] + heapq.heappop(hq)
                heapq.heappush(hq, -c[0])
        return len(hq)