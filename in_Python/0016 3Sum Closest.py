class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            cur = nums[i]
            dif = target - nums[i] - nums[i+1] - nums[i+2]
            a = i+1
            b = len(nums)-1
            while a < b:
                x = nums[a] 
                y = nums[b]
                if abs(target - cur - x - y) < abs(dif):
                    dif = target - cur - x - y
                if cur + x + y > target:
                    b -= 1
                elif cur + x + y == target:
                    return target
                else:
                    a += 1
            #print(dif)
            if len(res) == 0:
                res.append(dif)
            elif abs(dif) < abs(res[-1]):
                res[-1] = dif
        print(res)
        return target - res[-1]
            
                
            