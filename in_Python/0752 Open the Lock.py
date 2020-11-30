class Solution(object):
    def helper(self, s):
        res = []
        for i in range(len(s)):
            cur = int(s[i])
            if cur == 0:
                a = 9
                b = 1
            elif cur == 9:
                a = 8
                b = 0
            else:
                a = cur-1 
                b = cur+1
            res.append(s[:i] + str(a) + s[i+1:])
            res.append(s[:i] + str(b) + s[i+1:])
        return res
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        res = -1
        if target == '0000':
            return 0
        if '0000' in deadends:
            return res
        level = 0
        q = ['0000']
        seen = set()
        seen.add('0000')
        while q:
            n = len(q)
            while n != 0:
                n -= 1
                h = q.pop(0)
                for nex in self.helper(h):
                    if nex == target:
                        return level + 1
                    if nex not in seen and nex not in deadends:
                        q.append(nex)
                        seen.add(nex)
            level += 1
        return res
                    