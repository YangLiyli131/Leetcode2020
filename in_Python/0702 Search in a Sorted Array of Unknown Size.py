# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        i,j = 0, 10000
        while i < j:
            m = i + (j-i)/2
            if reader.get(m) == 2147483647:
                j = m
            else:
                i = m + 1
        L = i
        i,j = 0, L-1
        while i < j:
            m = i + (j-i)/2
            if reader.get(m) == target:
                return m
            elif  reader.get(m) < target:
                i += 1
            else:
                j -= 1
        if reader.get(i) == target:
            return i
        return -1