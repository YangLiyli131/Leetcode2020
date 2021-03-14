class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        n = len(word)
        if n not in self.d:
            self.d[n] = [word]
        else:
            self.d[n].append(word)
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.d:
            return False
        if '.' not in word:
            return word in self.d[len(word)]
        n = len(word)
        base = self.d[n]
        w = []
        idx = []
        for i,x in enumerate(word):
            if x != '.':
                w.append(x)
                idx.append(i)
        w = ''.join(w)
        for x in base:
            cur = []
            for y in idx:
                cur.append(x[y])
            cur = ''.join(cur)
            if w == cur:
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)