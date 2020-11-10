class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        s = S
        flag = [0] * len(s)
        for i in range(len(s)):
            maxL = 0
            for word in words:
                if s.startswith(word, i):
                    maxL = max(maxL, len(word))
            flag[i : i + maxL] = [1] * maxL
        res = []
        i = 0
        while i < len(s) and flag[i] == 0:
            res.append(s[i])
            i += 1
        j = i
        while j < len(s):
            while j < len(s) and flag[j] == 1:
                j += 1
            res.append('<b>')
            for x in range(i,j):
                res.append(s[x])
            res.append('</b>')
            if j == len(s):
                break
            while j < len(s) and flag[j] == 0:
                res.append(s[j])
                j += 1
            i = j
            j = i
        return ''.join(res)