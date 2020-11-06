class Solution(object):
    def transfer(self, x):
        value = 0
        if '0' <= x[0] <= '9':
            value += int(x[0]) * 16
        else:
            value += (ord(x[0]) - ord('a') + 10) * 16
        if '0' <= x[1] <= '9':
            value += int(x[1]) 
        else:
            value += ord(x[1]) - ord('a') + 10
        return value
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        base = ['00','11','22','33','44','55','66','77','88','99','aa','bb','cc','dd','ee','ff']
        vals = []
        for b in base:
            vals.append(self.transfer(b))
        sa = color[1:3]
        sb = color[3:5]
        sc = color[5:7]
        ss = [sa,sb,sc]
        res = ['#']
        for x in ss:
            value = self.transfer(x)
            mini_idx = 0
            dis = abs(vals[0] - value)
            for i in range(1, len(vals)):
                cur_val = vals[i]
                if abs(cur_val - value) < dis:
                    dis = abs(cur_val - value)
                    mini_idx = i
            res.append(base[mini_idx])
        return ''.join(res)
        