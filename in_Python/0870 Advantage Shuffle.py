class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = [0] * len(A)
        hp = []
        for i, b in enumerate(B):
            heapq.heappush(hp, [-b,i])
        A.sort()
        a = collections.deque()
        for ax in A:
            a.append(ax)
        while hp:
            v,idx = heapq.heappop(hp)
            vv = -v
            if a[-1] > vv:
                res[idx] = a.pop()
            else:
                res[idx] = a.popleft()
        return res