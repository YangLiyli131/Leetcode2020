class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = set()
        self.prex = set()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self.dict.add(word)
        for i in range(1, len(word)+1):
            self.prex.add(word[:i])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return word in self.dict

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return prefix in self.prex


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)