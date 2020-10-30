class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        text = text.split(' ')
        first = text[0]
        text[0] = first.lower()
        d = {}
        for i in range(len(text)):
            cur = text[i]
            L = len(cur)
            if L not in d:
                d[L] = [i]
            else:
                d[L].append(i)
        keys = d.keys()
        keys.sort()
        res = []
        for k in keys:
            row = d[k]
            for r in row:
                res.append(text[r])
        x = ' '.join(res)
        y = chr(ord('A') + ord(x[0]) - ord('a'))
        x = y + x[1:]
        return x