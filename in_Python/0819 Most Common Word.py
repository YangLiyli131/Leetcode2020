class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        d = {}
        maxfreq = 0
        maxword = ''
        i = 0
        while i < len(paragraph) and paragraph[i] in [' ','!','?',',','.',';','\'']:
            i += 1
        j = i 
        while j < len(paragraph):
            j = i
            while j < len(paragraph) and paragraph[j] not in [' ','!','?',',','.',';','\'']:
                j += 1
            word = paragraph[i:j]
            word = word.lower()
            if word != '' and word not in banned:
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1
            i = j
            while i < len(paragraph) and paragraph[i] in [' ','!','?',',','.',';','\'']:
                i += 1
        print(d)
        for k in d:
            if d[k] > maxfreq:
                maxfreq = d[k]
                maxword = k
        return maxword
            