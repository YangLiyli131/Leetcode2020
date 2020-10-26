class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        res = -1
        visited = [0] * N
        for i in range(N):
            if visited[i] == 1:
                continue
            counter = 0
            t = i
            while visited[t] != 1:
                visited[t] = 1
                t = nums[t]
                counter += 1
            res = max(res,counter)
        return res
            
        