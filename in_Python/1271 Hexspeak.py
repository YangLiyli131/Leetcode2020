class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        d = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        res = []
        num = int(num)
        while num != 0:
            cur = num % 16
            if 1 < cur < 10:
                return 'ERROR'
            else:
                if cur == 0:
                    res.insert(0, 'O')
                elif cur == 1:
                    res.insert(0,'I')
                else:
                    res.insert(0, d[cur])
            num /= 16
        return ''.join(res)