class Solution(object):
    def helper(self, s):
        if s[0] == '-':
            res = -int(s[1:-1])
        else:
            res = int(s[0:-1])
        return res
    
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = a.split('+')
        y = b.split('+')
        a1 = int(x[0])
        a2 = int(y[0])
        b1 = x[1]
        b2 = y[1]      
        
        res1 = self.helper(b1)
        res2 = self.helper(b2)
        
        c1 = a1 * a2 - res1 * res2
        c2 = a1 * res2 + a2 * res1
        res = str(c1) + '+' + str(c2) + 'i'

        return res
        
        