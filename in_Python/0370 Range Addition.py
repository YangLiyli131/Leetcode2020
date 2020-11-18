class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0] * length
        for update in updates:
            a = update[0]
            b = update[1]
            c = update[2]
            arr[a] += c
            if b < length-1:
                arr[b+1] -= c
        for i in range(1, length):
            arr[i] += arr[i-1]
        return arr
            