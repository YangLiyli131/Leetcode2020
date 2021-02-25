class Solution(object):
    def sortFeatures(self, features, responses):
        """
        :type features: List[str]
        :type responses: List[str]
        :rtype: List[str]
        """
        loc = {}
        for i,fe in enumerate(features):
            loc[fe] = i
        d = {}
        r = []
        for x in features:
            d[x] = 0
        for x in responses:
            xx = x.split(' ')
            ss = set(xx)
            for f in features:
                if f in ss:
                    d[f] += 1
        v = {}
        for k in d:
            va = d[k]
            if va not in v:
                v[va] = [k]
            else:
                v[va].append(k)
        vv = v.keys()  
        vv.sort(reverse = True)
        for x in vv:
            cur = v[x]
            if len(cur) > 1:
                tt = []
                for y in cur:
                    tt.append([loc[y],y])
                tt.sort()
                ttt = []
                for y in tt:
                    ttt.append(y[1])
                r += ttt
            else:
                r += cur
        return r