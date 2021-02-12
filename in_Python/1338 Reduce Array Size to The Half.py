class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        r = 1
        cur = 0
        d = collections.Counter(arr)
        va = d.values()
        va.sort(reverse = True)
        for x in va:
            cur += x
            if cur >= n/2:
                break
            r += 1
        return r
        
            