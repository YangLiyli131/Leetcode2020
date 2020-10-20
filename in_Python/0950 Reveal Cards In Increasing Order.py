class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck)
        deck.sort()
        res = [0] * n
        q = []
        for i in range(n):
            q.append(i)
        for i in range(n):
            res[q[0]] = deck[i]
            q = q[2:] + [q[1]] if len(q) > 1 else []
        return res