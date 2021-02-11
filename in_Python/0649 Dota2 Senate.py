class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        while 'R' in senate and 'D' in senate:
            preR, preD, actR, actD, bR, bD = collections.deque(),collections.deque(),collections.deque(),collections.deque(),collections.deque(),collections.deque()
            for i in range(len(senate)):
                if senate[i] == 'R':
                    actR.append(i)
                else:
                    actD.append(i)

            for i in range(len(senate)):
                cur = senate[i]
                if cur == 'R':
                    if i not in actR:
                        continue
                    if len(actD) != 0:
                        bD.append(actD.popleft())
                    elif len(preD) != 0:
                        bD.append(preD.popleft())
                    preR.append(actR.popleft())
                else:
                    if i not in actD:
                        continue
                    if len(actR) != 0:
                        bR.append(actR.popleft())
                    elif len(preR) != 0:
                        bR.append(preR.popleft())
                    preD.append(actD.popleft())
            tmp = []
            for idx in range(len(preR)):
                tmp.append([preR[idx],'R'])
            for idx in range(len(preD)):
                tmp.append([preD[idx],'D'])
            tmp.sort()
            ns = []
            for xx in tmp:
                ns.append(xx[1])
            senate = ''.join(ns)
            
        if 'D' in senate:
            return 'Dire'
        return 'Radiant'