class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = []
        dict = {}
        for x in cpdomains:
            t = x.split(' ')
            count = int(t[0])
            dnames = t[1].split('.')
            if len(dnames) == 3:
                s1 = dnames[1] + '.' + dnames[2]
                s2 = dnames[2]
                s3 = t[1]
                if s1 not in dict:
                    dict[s1] = count
                else:
                    dict[s1] += count
                if s2 not in dict:
                    dict[s2] = count
                else:
                    dict[s2] += count
                if s3 not in dict:
                    dict[s3] = count
                else:
                    dict[s3] += count
            else:
                s1 = dnames[1]
                s2 = t[1]
                if s1 not in dict:
                    dict[s1] = count
                else:
                    dict[s1] += count
                if s2 not in dict:
                    dict[s2] = count
                else:
                    dict[s2] += count                
        for k in dict:
            res.append(str(dict[k]) + ' ' + k)
        return res
                
        