class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        r = sum(cardPoints)
        cursum = [0]
        for i in range(len(cardPoints)):
            cursum.append(cursum[-1] + cardPoints[i])
        mx = sys.maxint
        l = len(cardPoints) - k
        for i in range(l, len(cardPoints)+1):
            d = cursum[i] - cursum[i - l]
            mx = min(mx, d)
        return r - mx
        