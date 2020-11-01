class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        d = {}
        for i in range(len(arr)):
            d[arr[i]] = i
        if len(pieces) == 1:
            return pieces[0] == arr
        seq = []
        dd = {}
        for p in pieces:
            first = p[0]
            if first not in d:
                return False
            idx = d[first]
            seq.append(idx)
            dd[idx] = p
        seq.sort()
        newarr = []
        for sq in seq:
            currow = dd[sq]
            for x in currow:
                newarr.append(x)
        return arr == newarr
        
            