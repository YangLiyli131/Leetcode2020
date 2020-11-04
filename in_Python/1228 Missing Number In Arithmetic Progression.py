class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d = None
        pre = None
        for i in range(1, len(arr)):
            df = arr[i] - arr[i-1]
            if not d:
                d = df
                pre = arr[i-1]
            else:
                if df == d + d:
                    return arr[i-1] + d
                elif d == df + df:
                    return pre + df
        return arr[0]
                    
        