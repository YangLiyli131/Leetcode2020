class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        visited = set()
        bank = set(bank)
        if end not in bank:
            return -1
        q = [(start, 0)]
        while q:
            gene, count = q.pop(0)
            if gene == end:
                return count
            if gene in visited:
                continue
            for gi in range(len(gene)):
                for j in ['A','G','C','T']:
                    newgene = gene[:gi] + j + gene[gi+1:]
                    if newgene in bank:
                        q.append((newgene,count+1))
            visited.add(gene)
        return -1