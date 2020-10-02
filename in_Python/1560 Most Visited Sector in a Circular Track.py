class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        d = {}
        d[rounds[0]] = 1
        for i in range(1,len(rounds)):
            a = rounds[i-1]
            b = rounds[i]
            if a < b:
                for j in range(a+1, b+1):
                    if j not in d:
                        d[j] = 1
                    else:
                        d[j] += 1
            else:
                b += n
                for j in range(a+1, b+1):
                    if j <= n:
                        if j not in d:
                            d[j] = 1
                        else:
                            d[j] += 1
                    else:
                        j = j % n
                        if j not in d:
                            d[j] = 1
                        else:
                            d[j] += 1
        res = []
        m = -1
        for k in d:
            if d[k] > m:
                res = []
                m = d[k]
                res.append(k)
            elif d[k] == m:
                res.append(k)
            else:
                continue
        res.sort()
        return res
                
            
        