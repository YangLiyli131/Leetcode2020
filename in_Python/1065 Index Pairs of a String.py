class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        for w in words:
            L = len(w)
            i = 0
            j = L
            while j <= len(text):
                if text[i : j] == w:
                    res.append([i,j-1])
                i += 1
                j = i + L
        res = sorted(res, key = lambda x : (x[0],x[1]))
        return res