class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(s)):
            if s[i] == 'I':
                res += list(range(i+1, len(res), -1))
        res += list(range(len(s)+1, len(res), -1))
        return res




class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        base = set(list(range(1, n+2)))
        bt = []
        for i in range(1, n+2):
            bt.append([i])
        added = True
        idx = 0
        while added and idx < len(s):
            added = False
            cur = []
            order = s[idx]
            idx += 1
            for pre in bt:
                last = pre[-1]
                existed = set(pre)
                if order == 'I':
                    for i in range(1, n+2):
                        if i not in existed and i > last:
                            tmp = pre + [i]
                            cur.append(tmp)
                            added = True
                else:
                    for i in range(1, n+2):
                        if i not in existed and i < last:
                            tmp = pre + [i]
                            cur.append(tmp)
                            added = True
                cur.append(pre)
            bt = cur
        res = None
        for x in bt:
            if len(x) == n+1:
                if res == None:
                    res = x
                else:
                    if x < res:
                        res = x
        return res
                        
        