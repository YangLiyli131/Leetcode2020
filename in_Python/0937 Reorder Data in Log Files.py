class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        d = {}
        for i in range(len(logs)):
            cur = logs[i]
            curarr = cur.split(' ')
            if '0' <= curarr[1][0] <= '9':
                digits.append(cur)
            else:    
                key = ''
                for j in range(1, len(curarr)):
                    key += curarr[j] + ' '
                key += curarr[0]
                d[key] = i
        res = []
        keys = d.keys()
        keys.sort()
        for k in keys:
            idx = d[k]
            res.append(logs[idx])
        for x in digits:
            res.append(x)
        return res