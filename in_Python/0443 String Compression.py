class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        idx = 0
        j = 0
        N = len(chars)
        while j < N:
            j = i + 1
            while j < N and chars[j] == chars[i]:
                j += 1
            d = j - i
            if d == 1:
                chars[idx] = chars[i]
                idx += 1
            else:
                chars[idx] = chars[i]
                idx += 1
                if d < 10:
                    chars[idx] = str(d)
                    idx += 1
                else:
                    d = list(str(d))
                    for x in d:
                        chars[idx] = x
                        idx += 1
            i = j
        return idx