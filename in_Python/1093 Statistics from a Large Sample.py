class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        N = sum(count)
        i = 0
        mini, maxi = None, None
        while i < len(count):
            if count[i] != 0:
                mini = i
                break
            i += 1
        j = len(count)-1
        while j >= 0:
            if count[j] != 0:
                maxi = j
                break
            j -= 1
        most, mod = 0,0
        for i,x in enumerate(count):
            if x > most:
                most = x
                mod = i
        
        s = 0
        for i,x in enumerate(count):
            s += i * x
        ave = s / float(N)
        cursum = 0
        md = None
        next = False
        pre = None
        for i,x in enumerate(count):
            if next:
                md = i
                break
            if pre:
                md = (pre + i) / float(2)
                break
            if cursum + x > N/2:
                md = i
                break
            elif cursum + x < N/2:
                cursum += x
            else:
                if N % 2 != 0:
                    next = True
                else:
                    pre = i
        return [float(mini),float(maxi),ave, md, float(mod)]