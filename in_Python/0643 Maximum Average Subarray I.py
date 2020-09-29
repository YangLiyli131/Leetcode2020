class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        j = k-1
        best = [i,j]
        cursum = 0
        for x in range(k):
            cursum += nums[x]        
        maxsum = cursum
        while j < len(nums)-1:
            newsum = cursum - nums[i] + nums[j+1]
            if newsum > maxsum:
                maxsum = newsum
                best[0] = i+1
                best[1] = j+1
            cursum = newsum
            i += 1
            j += 1
        return maxsum / float(k)