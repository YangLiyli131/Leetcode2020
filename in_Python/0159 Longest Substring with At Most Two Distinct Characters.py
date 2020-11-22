class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        i,j = 0,0
        res = 0
        while j < len(s):
            while j < len(s) and len(counter) <= 2:
                cur = s[j]
                if cur in counter:
                    counter[cur] += 1
                    j += 1
                else:
                    if len(counter) < 2:
                        counter[cur] = 1
                        j += 1
                    else:
                        break
            res = max(res, j-i)
            
            while len(counter) == 2:
                cur = s[i]
                counter[cur] -= 1
                if counter[cur] == 0:
                    counter.pop(cur, 'None')
                i += 1
        return res
            