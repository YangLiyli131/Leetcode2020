class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        d = {}
        d[nums[0]] = [0]
        for i in range(1, len(nums)):
            cursum = nums[i-1] + nums[i]
            if cursum not in d:
                t = [i]
                d[cursum] = t
            else:
                t = d[cursum]
                t.append(i)
                d[cursum] = t
            nums[i] = cursum
        #print(d)
        if k in d:
            res += len(d[k])
        if k == 0:
            for key in d:
                n = len(d[key])
                res += n * (n-1) / 2
        else:
            for key in d:
                a = d[key]
                if key + k in d:
                    b = d[key+k]
                    for x in a:
                        for y in b:
                            if y > x:
                                res += 1
        return res