class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        m,n = len(word1),len(word2)
        i,j = 0,0
        r = []
        while i < m and j < n:
            if word1[i] > word2[j]:
                r.append(word1[i])
                i += 1
            elif word1[i] < word2[j]:
                r.append(word2[j])
                j += 1
            else:
                if word1[i:] < word2[j:]:
                    r.append(word2[j])
                    j += 1
                else:
                    r.append(word1[i])
                    i += 1
        while i < m:
            r.append(word1[i])
            i += 1
        while j < n:
            r.append(word2[j])
            j += 1
        return ''.join(r)