class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        res = []
        for i in range(arr[0]-1):
            res.append(i+1)
        for i in range(1, len(arr)):
            pre = arr[i-1]
            cur = arr[i]
            for idx in range(pre+1, cur):
                res.append(idx)
        if len(res) >= k:
            return res[k-1]
        else:
            last = arr[-1]
            dif = k - len(res)
            while dif != 0:
                dif -= 1
                last += 1
            return last