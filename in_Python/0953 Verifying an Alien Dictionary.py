class Solution(object):
    def isSmaller(self,a,b,order):
        i,j = 0,0
        while i < len(a) and j < len(b):
            x = order.index(a[i])
            y = order.index(b[j])
            if x > y:
                return False
            if x < y:
                return True
            i += 1
            j += 1
        if i < len(a):
            return False
        return True
            
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(1,len(words)):
            if not self.isSmaller(words[i-1],words[i], order):
                return False
        return True
