class Trie(object):

    def __init__(self):
        self.word = {}
        self.pre = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if word not in self.word:
            self.word[word] = 1
        else:
            self.word[word] += 1
        for i in range(1, len(word)+1):
            p = word[:i]
            if p not in self.pre:
                self.pre[p] = {}
            if word not in self.pre[p]:
                self.pre[p][word] = 1
            else:
                self.pre[p][word] += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        if word not in self.word:
            return 0
        return self.word[word]

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        if prefix not in self.pre:
            return 0
        return sum(self.pre[prefix].values())

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.word[word] -= 1
        for i in range(1, len(word)+1):
            p = word[:i]
            if p not in self.pre:
                continue
            row = self.pre[p]
            if word in row:
                row[word] -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)