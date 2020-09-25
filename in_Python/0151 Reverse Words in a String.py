class Solution(object):        
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        word = s.split(' ')
        words = []
        for w in word:
            if w == '':
                continue
            words.insert(0,w)
        #print(words)
        newwords = ''
        for w in words:
            #ne = self.rev(w)
            newwords += w
            newwords += ' '
        
        return newwords.strip()