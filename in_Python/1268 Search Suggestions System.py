class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        trie = {}
        for p in products:
            for i in range(1,len(p)+1):
                prex = p[:i]
                if prex not in trie:
                    trie[prex] = [p]
                else:
                    trie[prex].append(p)
        res = []
        for i in range(1, len(searchWord)+1):
            key = searchWord[:i]
            if key not in trie:
                res.append([])
                continue
            candidates = trie[key]
            candidates.sort()
            if len(candidates) <= 3:
                res.append(candidates)
            else:
                res.append(candidates[:3])
        return res