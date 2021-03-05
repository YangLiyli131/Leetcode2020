class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        base = collections.Counter(letters)
        sc = {}
        ss = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            sc[ss[i]] = score[i]
        can = [[]]
        added = True
        idx = 0
        while idx < len(words):
            added = False
            tmp = []
            w = words[idx]
            for pre in can:
                tmp.append(pre)
                pree = pre[:]
                pree.append(w)
                tmp.append(pree)
            idx += 1
            can = tmp
        cur = []
        r = 0
        
        def value(s):
            res = 0
            for xx in s:
                res += sc[xx]
            return res
        def check(d1,d2):
            for k in d1:
                if k not in d2 or d1[k] > d2[k]:
                    return False
            return True
        
        for x in can:
            cur.append(''.join(x))
        for x in cur:
            d = collections.Counter(x)
            if check(d, base):
                val = value(x)
                r = max(r, val)
        return r
                