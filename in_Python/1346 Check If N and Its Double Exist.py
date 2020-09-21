class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}
        for ii in range(len(arr)):
            i = arr[ii]
            if i*2 in dict and dict[i*2] != ii:
                return True
            if i % 2 == 0 and i/2 in dict and dict[i/2] != ii:
                return True
            dict[i] = ii
        return False