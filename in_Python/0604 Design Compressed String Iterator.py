class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.letter_idx = []
        self.letters = []
        for i in range(len(compressedString)):
            if 'a' <= compressedString[i] <= 'z' or 'A' <= compressedString[i] <= 'Z':
                self.letter_idx.append(i)
                self.letters.append(compressedString[i])
        self.letter_nums = []
        begin = 0
        end = 0
        for i in range(1, len(self.letter_idx)):
            begin = self.letter_idx[i-1] + 1
            end = self.letter_idx[i]
            self.letter_nums.append(int(compressedString[begin: end]))
        self.letter_nums.append(int(compressedString[end+1:]))
        
        self.total = sum(self.letter_nums)
        self.numid = 0
        self.letterid = 0
        self.num_print = 0
        self.curletter = self.letters[self.letterid]
        self.curcount = self.letter_nums[self.numid]
        
    def next(self):
        """
        :rtype: str
        """
        if self.curcount != 0:
            self.curcount -= 1
            self.num_print += 1
            return self.curletter
        self.letterid += 1
        self.numid += 1
        if self.letterid >= len(self.letters):
            return ' '
        self.curletter = self.letters[self.letterid]
        self.curcount = self.letter_nums[self.numid]
        self.curcount -= 1
        self.num_print += 1
        return self.curletter
        
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.num_print < self.total


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()