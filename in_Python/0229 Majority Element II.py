class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter1, counter2, can1, can2 = 0,0,0,0
        for i in nums:
            if i == can1:
                counter1 += 1
            elif i == can2:
                counter2 += 1
            elif counter1 == 0:
                can1 = i
                counter1 = 1
            elif counter2 == 0:
                can2 = i
                counter2 = 1
            else:
                counter2 -= 1
                counter1 -= 1
        counter1, counter2 = 0,0
        for i in nums:
            if i == can1:
                counter1 += 1
            elif i == can2:
                counter2 += 1
        print([can1,can2])
        if counter1 > len(nums)//3 and counter2 > len(nums)//3:
            return [can1, can2]
        elif counter1 > len(nums)//3:
            return [can1]
        elif counter2 > len(nums)//3:
            return [can2]
        else:
            return []