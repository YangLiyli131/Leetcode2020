Trie = lambda : collections.defaultdict(Trie)
WEIGHT = False
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        for w, wo in enumerate(words):
            wo += '#'
            for i in range(len(wo)):
                cur = self.trie
                cur[WEIGHT] = w
                for j in range(i, 2 * len(wo) - 1):
                    cur = cur[wo[j % len(wo)]]
                    cur[WEIGHT] = w

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        cur = self.trie
        for le in suffix + '#' + prefix:
            if le not in cur:
                return -1
            cur = cur[le]
        return cur[WEIGHT]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)