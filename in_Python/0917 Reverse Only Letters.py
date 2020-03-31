class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        SS = []
        for i in range(len(S)): SS.append(S[i])
        i = 0
        j = len(S)-1
        while i < j:
            while not S[i].isalpha() and i < len(S)-1:
                i += 1
            while not S[j].isalpha() and j >= 0:
                j -= 1
            if i >= j:
                break
            temp = SS[i]
            SS[i] = SS[j]
            SS[j] = temp
            i += 1
            j -= 1
        res = ""
        for x in SS:
            res += x
        return res
            
        