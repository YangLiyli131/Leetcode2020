class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        p = 0
        while n != 0:
            c = n % 2
            n /= 2
            res += c  * pow(2, 31 - p)
            p += 1
        return res