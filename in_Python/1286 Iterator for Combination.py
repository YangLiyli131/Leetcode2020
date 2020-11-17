class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.pool = []
        
        def dfs(n, s, cur):
            if len(cur) == n:
                self.pool.append(''.join(cur))
                return
            for i in range(s, len(characters)):
                cur.append(characters[i])
                dfs(n, i+1, cur)
                cur.pop()
        
        dfs(combinationLength, 0, [])
        
        self.idx = 0
        
    def next(self):
        """
        :rtype: str
        """
        t = self.pool[self.idx]
        self.idx += 1
        return t

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.pool)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()