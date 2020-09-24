class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        i = len(a)-1
        j = len(b)-1
        c = 0
        res = ""
        while i >= 0 or j >= 0:
            if i >= 0:
                x = int(a[i])
            else:
                x = 0
            if j >= 0:
                y = int(b[j])
            else:
                y = 0
            z = x + y + c
            res = str(z % 2) + res
            c = z / 2
            i -= 1
            j -= 1
        if c == 1:
            res = '1' + res
        return res
        