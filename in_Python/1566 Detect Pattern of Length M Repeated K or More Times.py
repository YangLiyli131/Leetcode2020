class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        for i in range(0, len(arr)-m):
            cur = arr[i : i + m]
            counter = 1
            i += m
            while i + m <= len(arr):
                nex = arr[i : i + m]
                if nex == cur:
                    counter += 1
                    i += m
                    if counter == k:
                        return True
                else:
                    break
        return False

            