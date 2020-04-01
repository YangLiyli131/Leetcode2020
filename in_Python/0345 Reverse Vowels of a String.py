class Solution(object):
    def isV(self,a):
        return a in ['a','e','i','o','u','A','E','I','O','U']
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s)-1
        
        ss = []
        for x in s: ss.append(x)
        
        while i < j:
            while not self.isV(s[i]) and i < j:
                i += 1
            while not self.isV(s[j]) and i < j:
                j -= 1
            t = ss[i]
            ss[i] = ss[j]
            ss[j] = t
            i += 1
            j -= 1
            
        res = ""
        for x in ss: res += x
        return res
    