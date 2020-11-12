class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        d = {}
        res = []
        for i in range(len(keyName)):
            name = keyName[i]
            time = keyTime[i]
            hour = int(time[0:2])
            mini = int(time[3:5])
            total = hour * 60 + mini
            if name not in d:
                d[name] = [total]
            else:
                d[name].append(total)
        for k in d:
            cur = d[k]
            cur.sort()
            d[k] = cur
        for k in d:
            cur = d[k]
            if len(cur) < 3:
                continue
            for i in range(len(cur)-2):
                if cur[i+2] - cur[i] <= 60:
                    res.append(k)
                    break
        res.sort()
        return res