class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        t = []
        res = 0
        for i in A:
            if i not in t: 
                t.append(i)
            else:
                res = i
                break
        return res
        