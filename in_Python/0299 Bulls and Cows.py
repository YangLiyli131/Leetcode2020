class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        nb = 0
        nc = 0
        d1 = {}
        d2 = {}
        for i in range(len(secret)):
            n = secret[i]
            if n not in d1:
                t = []                
            else:
                t = d1[n]
            t.append(i)
            d1[n] = t
        for i in range(len(guess)):
            n = guess[i]
            if n not in d2:
                t = []                
            else:
                t = d2[n]
            t.append(i)
            d2[n] = t   
        for k in d2:
            if k not in d1:
                continue
            loc = d2[k]
            tar = d1[k]
            b = min(len(loc), len(tar))
            thisnb = 0
            for l in loc:
                if l in tar:
                    thisnb += 1
            nb += thisnb
            nc += b - thisnb
        return str(nb) + 'A' + str(nc) + 'B'
        
        