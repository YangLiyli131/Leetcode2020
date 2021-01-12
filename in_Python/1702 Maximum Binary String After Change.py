class Solution(object):
    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        res = []
        i = 0
        n = len(binary)
        while i < n and binary[i] == '1':
            res.append('1')
            i += 1
        z = 0
        o = 0
        idx = i
        while i < n: 
            x = binary[i]
            if x == '0':
                z += 1
            else:
                o += 1
            i += 1
            res.append('1')
        if z == 0:
            return ''.join(res)
        res[idx + z - 1] = '0'
        return ''.join(res)
        