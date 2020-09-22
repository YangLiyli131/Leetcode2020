class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        t = set()
        for i in arr:
            if i not in t:
                t.add(i)
        tt = []
        for i in t:
            tt.append(i)
        tt.sort()
        d = {}
        for i in range(len(tt)):
            d[tt[i]] = i+1
        for i in range(len(arr)):
            arr[i] = d[arr[i]]
        return arr