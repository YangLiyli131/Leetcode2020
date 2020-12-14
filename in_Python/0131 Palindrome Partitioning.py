class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def bt(start, end, tmp):
            if start == end:
                res.append(tmp[:])
            for i in range(start, end):
                cur = s[start : i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    bt(i+1, end, tmp)
                    tmp.pop()
        res = []
        bt(0, len(s), [])
        return res