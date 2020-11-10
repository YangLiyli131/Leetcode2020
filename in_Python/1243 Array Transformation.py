class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ops = 1
        while ops != 0:
            ops = 0
            tmp = [arr[0]]
            for i in range(1,len(arr)-1):
                cur = arr[i]
                if cur > arr[i-1] and cur > arr[i+1]:
                    ops = 1
                    tmp.append(cur-1)
                elif cur < arr[i-1] and cur < arr[i+1]:
                    ops = 1
                    tmp.append(cur+1)
                else:
                    tmp.append(cur)
            tmp.append(arr[-1])
            arr = tmp
        return arr