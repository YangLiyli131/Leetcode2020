class Solution(object):
    def isC(self,c):
        if c >= 'A' and c <= 'Z':
            return True
        return False
    
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        first_letter_cap = self.isC(word[0])
        total = 0
        if first_letter_cap:
            total += 1
        for i in range(1,len(word)):
            cur = self.isC(word[i])
            if cur: total += 1
        if total == len(word) or (first_letter_cap and total == 1) or total == 0:
            return True
        else:
            return False
            
        