class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        allsyn = set()
        adj = {}
        for i in range(len(synonyms)):
            a = synonyms[i][0]
            b = synonyms[i][1]
            if a not in adj:
                adj[a] = [b]
            else:
                adj[a].append(b)
            if b not in adj:
                adj[b] = [a]
            else:
                adj[b].append(a)
            allsyn.add(a)
            allsyn.add(b)
        bases = []
        visited = set()
        for x in list(allsyn):
            if x in visited:
                continue
            visited.add(x)
            comp = [x]
            q = adj[x]
            while q:
                head = q.pop(0)
                comp.append(head)
                if head not in visited:
                    visited.add(head)
                    for nex in adj[head]:
                        if nex not in visited:
                            q.append(nex)
            bases.append(comp)

        tx = text.split(' ')   
        N = len(tx)
        res = [[]]
        for word in tx:
            tmp = []
            if word not in allsyn:
                for x in res:
                    x.append(word)
                    tmp.append(x)
                res = tmp
            else:
                for base in bases:
                    if word in base:
                        for x in res:
                            for ba in base:
                                y = x[:]
                                y.append(ba)
                                tmp.append(y)
                        res = tmp
                        break
            #print(res)
        result = []
        for x in res:
            result.append(' '.join(x))
        result.sort()
        return result
                        
            