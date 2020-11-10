class Solution(object):
    def buddyStrings(self, A, B):
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
        if A == B:
            d = {}
            for a in A:
                if a not in d:
                    d[a] = 1
                else:
                    d[a] += 1
            valid = 0
            for k in d:
                if d[k] > 1:
                    valid = 1
                    break
            if valid == 0:
                return False
            else:
                return True        
        dif = []
        for i in range(len(A)):
            if A[i] != B[i]:
                dif.append(i)
        if len(dif) != 2:
            return False
        d1 = dif[0]
        d2 = dif[1]
        return A[d1] == B[d2] and B[d1] == A[d2]
        