class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0
        if not word1 and word2:
            return len(word2)
        if not word2 and word1:
            return len(word1)
        m,n = len(word1), len(word2)
        g = []
        for i in range(m+1):
            cur = [0] * (n+1)
            g.append(cur)   
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    g[i][j] = g[i-1][j-1] + 1
                else:
                    g[i][j] = max(g[i-1][j], g[i][j-1])
        return m + n - 2 * g[-1][-1]