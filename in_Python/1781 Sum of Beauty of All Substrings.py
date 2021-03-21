class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        count = []
        init = [0] * 26
        count.append(init)
        for x in s:
            init = count[-1][:]
            dif = ord(x) - ord('a')
            init[dif] += 1
            count.append(init)
            
        for i in range(len(count)):
            for j in range(i+1, len(count)):
                d = set()
                for idx in range(26):
                    d.add(count[j][idx] - count[i][idx])
                if 0 in d:
                    d.remove(0)
                if not d:
                    continue
                r += max(d)-min(d)
                
        return r