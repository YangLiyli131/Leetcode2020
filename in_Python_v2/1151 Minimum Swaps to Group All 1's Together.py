class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        ones = sum(data)
        if ones <= 1:
            return 0
        no = sum(data[:ones])
        nz = ones - no
        res = nz
        i = 0
        j = ones
        while j < len(data):
            if data[i] == 0:
                nz -= 1
            else:
                no -= 1
            if data[j] == 0:
                nz += 1
            else:
                no += 1
            res = min(res, nz)
            i += 1
            j += 1
        return res
            