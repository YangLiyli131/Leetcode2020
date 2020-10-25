class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        res = keysPressed[0]
        count = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            curletter = keysPressed[i]
            curtime = releaseTimes[i] - releaseTimes[i-1]
            if curtime > count:
                count = curtime
                res = curletter
            elif curtime == count:
                if curletter > res:
                    res = curletter
        return res