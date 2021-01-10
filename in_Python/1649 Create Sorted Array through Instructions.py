from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions):
        SList = SortedList()
        ans = 0
        for num in instructions:
            ans += min(SList.bisect_left(num), len(SList) - SList.bisect_right(num))
            ans %= (10**9 + 7)
            SList.add(num)

        return ans

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        arr = [instructions[0]]
        cost = 0
        for x in instructions[1:]:
            left = bisect.bisect_left(arr, x)
            right = bisect.bisect_right(arr, x)
            cost += min(left, len(arr) - right)
            bisect.insort(arr,x)
            cost % (1000000007)
        return cost % (1000000007)