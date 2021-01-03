class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        res = []
        f = 1
        if a < 0:
            f = -1
        if a == 0:
            if b > 0:
                for x in nums:
                    res.append(b * x + c)
                return res
            elif b < 0:
                for x in nums:
                    res.insert(0, b * x + c)
                return res
            else:
                return [c] * len(nums)
        z = -b/float(2*a)
        if z <= nums[0]:
            if f == 1:
                for x in nums:
                    res.append(a * x * x + b * x + c)
            else:
                for x in nums:
                    res.insert(0, a * x * x + b * x + c)
            return res
        if z >= nums[-1]:
            if f == 1:
                for x in nums:
                    res.insert(0, a * x * x + b * x + c)
            else:
                for x in nums:
                    res.append(a * x * x + b * x + c)
            return res            
        idx = -1
        dis = sys.maxint
        for i in range(len(nums)):
            if abs(nums[i] - z) < dis:
                dis = abs(nums[i] - z)
                idx = i
        if f == 1:
            res.append(a * nums[idx] * nums[idx] + b * nums[idx] + c)
            left, right = idx - 1, idx + 1
            while left >= 0 and right < len(nums):
                if abs(nums[left] - z) < abs(nums[right] - z):
                    res.append(a * nums[left] * nums[left] + b * nums[left] + c)
                    left -= 1
                else:
                    res.append(a * nums[right] * nums[right] + b * nums[right] + c)
                    right += 1
            while left >= 0:
                res.append(a * nums[left] * nums[left] + b * nums[left] + c)
                left -= 1
            while right < len(nums):
                res.append(a * nums[right] * nums[right] + b * nums[right] + c)
                right += 1
        else:
            res.insert(0, a * nums[idx] * nums[idx] + b * nums[idx] + c)
            left, right = idx - 1, idx + 1
            while left >= 0 and right < len(nums):
                if abs(nums[left] - z) < abs(nums[right] - z):
                    res.insert(0, a * nums[left] * nums[left] + b * nums[left] + c)
                    left -= 1
                else:
                    res.insert(0, a * nums[right] * nums[right] + b * nums[right] + c)
                    right += 1
            while left >= 0:
                res.insert(0, a * nums[left] * nums[left] + b * nums[left] + c)
                left -= 1
            while right < len(nums):
                res.insert(0, a * nums[right] * nums[right] + b * nums[right] + c)
                right += 1
        return res
                    