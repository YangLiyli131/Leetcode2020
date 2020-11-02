class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        idx = 0
        t = 0
        while idx < len(arr):
            if t + arr[idx] <= 5000:
                t += arr[idx]
                idx += 1
            elif t + arr[idx] > 5000:
                break
        return idx
        