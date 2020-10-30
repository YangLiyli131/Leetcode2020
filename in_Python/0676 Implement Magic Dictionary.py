class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = set()
        

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for x in dictionary:
            self.d.add(x)

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        for x in self.d:
            if self.check(searchWord, x):
                return True
        return False
    def check(self, a, b):
        if len(a) != len(b):
            return False
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
            if diff > 1:
                return False
        return diff == 1


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)