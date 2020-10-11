class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        loc = [0]
        while i < len(bits):
            if bits[i] == 1:
                i += 2
            else:
                i += 1
            loc.append(i)
        return len(bits)-1 in loc