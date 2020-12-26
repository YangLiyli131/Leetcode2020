class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        lst = collections.deque()
        res = []
        for x in number:
            if x not in [' ', '-']:
                lst.append(x)
        total = len(lst)
        while total > 4:
            res.append(lst.popleft())
            res.append(lst.popleft())
            res.append(lst.popleft())
            res.append('-')
            total -= 3
        if total == 4:
            res.append(lst.popleft())
            res.append(lst.popleft())
            res.append('-')
            res.append(lst.popleft())
            res.append(lst.popleft())
        elif total == 3:
            res.append(lst.popleft())
            res.append(lst.popleft())
            res.append(lst.popleft())
        else:
            res.append(lst.popleft())
            res.append(lst.popleft())
        return ''.join(res)