class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == None and B == None:
            return True
        if A == None or B == None:
            return False
        if len(A) != len(B):
            return False
        if len(A) == 0 and len(B) == 0:
            return True
        nb = B + B
        #print(nb)
        for i in range(len(nb)):
            j = i + len(A)
            if j > len(nb):
                return False
            if nb[i:j] == A:
                return True
        return False