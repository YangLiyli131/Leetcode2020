class ValidWordAbbr(object):
    def abv(self, w):
        res = []
        res.append(w[0])
        res.append(str(len(w)-2))
        res.append(w[-1])
        return ''.join(res)
        
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.map = {}
        for x in dictionary:
            abv = self.abv(x)
            if abv not in self.map:
                self.map[abv] = [x]
            else:
                self.map[abv].append(x)
        print(self.map)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        wabv = self.abv(word)
        if wabv not in self.map:
            return True
        else:
            for x in self.map[wabv]:
                if x != word:
                    return False
            return True


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)