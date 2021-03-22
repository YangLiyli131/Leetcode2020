class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        words = {}
        for w in wordlist:
            words[w] = w
        cap = {}
        for w in wordlist[::-1]:
            cap[w.lower()] = w
        vow = {}
        for wi in wordlist[::-1]:
            w = wi.lower()
            t = []
            for x in w:
                if x not in 'aeiuo':
                    t.append(x)
                else:
                    t.append('#')
            vow[''.join(t)] = wi
        r = []
        for q in queries:
            if q in words:
                r.append(words[q])
                continue
            if q.lower() in cap:
                r.append(cap[q.lower()])
                continue
            qt = []
            for x in q.lower():
                if x not in 'aeiuo':
                    qt.append(x)
                else:
                    qt.append('#')
            qtt = ''.join(qt)
            if qtt in vow:
                r.append(vow[qtt])
                continue
            r.append('')
        return r
        