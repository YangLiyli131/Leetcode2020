class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = []
        l2 = []
        for s in s1:
            l1.append(s)
        for s in s2:
            l2.append(s)
        l1.sort()
        l2.sort()
        i = 0
        while i < len(l1) and l1[i] == l2[i]:
            i += 1
        a = l1[i]
        b = l2[i]
        for i in range(i,len(l1)):
            if a > b and l1[i] < l2[i]:
                return False
            if a < b and l1[i] > l2[i]:
                return False
        return True
