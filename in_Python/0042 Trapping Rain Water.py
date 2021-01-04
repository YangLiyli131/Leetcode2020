class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left_max, right_max = 0, 0
        i, j = 0, len(height)-1
        while i < j:
            if height[i] < height[j]:
                if left_max < height[i]:
                    left_max = height[i]
                else:
                    res += left_max - height[i]
                i += 1
            else:
                if right_max < height[j]:
                    right_max = height[j]
                else:
                    res += right_max - height[j]
                j -= 1
        return res