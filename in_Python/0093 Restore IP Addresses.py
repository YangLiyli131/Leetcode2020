class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        li = [[[], s, 4]]
        res = []
        added = True
        while added:
            added = False
            newli = []
            for x in li:              
                r = x[0]
                st = x[1]
                idx = x[2]
                if st == '' and idx == 0:
                    res.append(r[:])
                if idx < 0:
                    continue
                if idx == 0 and st != '':
                    continue
                i = 1
                while i < len(st)+1:
                    first = st[:i]

                    if int(first) > 255:
                        break
                    sec = st[i:]
                    if first == '0' or first[0] != '0':
                        rr = r[:] 
                        if len(rr) != 0:
                            rr.append('.')
                        rr.append(first)
                        newli.append([rr, sec, idx-1])
                        added = True
                    i += 1
            li = newli
        rt = []
        for x in res:
            rt.append(''.join(x))
        return rt
