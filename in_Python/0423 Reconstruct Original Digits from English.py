class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)
        z = [0] * 10
        if 'z' in count:
            d = count['z']
            z[0] += d
            count['e'] -= d
            count['r'] -= d
            count['o'] -= d
        if 'x' in count:
            d = count['x']
            z[6] += d
            count['s'] -= d
            count['i'] -= d
        if 'w' in count:
            d = count['w']
            z[2] += d
            count['o'] -= d
            count['t'] -= d
        if 'u' in count:
            d = count['u']
            z[4] += d
            count['f'] -= d
            count['r'] -= d
            count['o'] -= d
        if 'f' in count:
            d = count['f']
            z[5] += d
            count['e'] -= d
            count['i'] -= d
            count['v'] -= d
        if 'v' in count:
            d = count['v']
            z[7] += d
            count['e'] -= d * 2
            count['s'] -= d
            count['n'] -= d
        if 'o' in count:
            d = count['o']
            z[1] += d
            count['e'] -= d
            count['n'] -= d
        if 'n' in count:
            d = count['n']
            z[9] += d // 2
            count['i'] -= d // 2
            count['e'] -= d // 2
        if 'i' in count:
            d = count['i']
            z[8] += d 
            count['g'] -= d
            count['e'] -= d
            count['h'] -= d
            count['t'] -= d
        z[3] = count['t']
        r = []
        for i,x in enumerate(z):
            while x != 0:
                x -= 1
                r.append(str(i))
        return ''.join(r)