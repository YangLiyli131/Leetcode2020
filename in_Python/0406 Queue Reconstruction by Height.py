class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        r = []
        d = {}
        for p in people:
            h,i = p[0], p[1]
            if h not in d:
                d[h] = [i]
            else:
                d[h].append(i)
        for k in d:
            t = d[k]
            t = sorted(t)
            d[k] = t
        keys = d.keys()
        keys.sort(reverse = True)
        for k in keys:
            cur = d[k]
            for i in cur:
                if i == 0:
                    r.insert(0, [k,i])
                elif i >= len(r):
                    r.append([k,i])
                else:
                    r = r[:i] + [[k,i]] + r[i:]
        return r