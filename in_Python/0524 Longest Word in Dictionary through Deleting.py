class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        dd = {}
        for si in range(len(s)):
            cur = s[si]
            if cur not in dd:
                dd[cur] = [si]
            else:
                dd[cur].append(si)
        res = ''
        for w in d:
            minim = -1
            for c in w:
                if c not in dd:
                    minim = -1
                    break
                for i in dd[c]:
                    found = 0
                    if i > minim:
                        minim = i
                        found = 1
                        break
                if found == 0:
                    minim = -1
                    break
            if minim != -1:
                if len(res) < len(w):
                    res = w
                elif len(res) == len(w):
                    res = min(res,w)
        return res
                    