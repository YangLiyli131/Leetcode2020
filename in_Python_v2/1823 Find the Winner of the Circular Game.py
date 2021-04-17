class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        q = collections.deque()
        for i in range(1, n+1):
            q.append(i)
        counter = 0
        while len(q) != 1:
            h = q.popleft()
            counter += 1
            if counter == k:
                counter = 0
            else:
                q.append(h)
        return q[0]