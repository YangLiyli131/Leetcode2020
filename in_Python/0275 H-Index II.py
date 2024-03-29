class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        buckets = []
        n = len(citations)
        for i in range(n+1):
            buckets.append(0)
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
        count = 0
        for i in range(n, -1, -1):
            count += buckets[i]
            if count >= i:
                return i
        return 0