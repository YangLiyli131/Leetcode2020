class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands = ["","Thousand","Million","Billion"]
        
        res = ''
        if num == 0:
            return 'Zero'
        
        def helper(n):
            if n == 0:
                return ''
            elif n < 20:
                return lessThan20[n] + ' '
            elif n < 100:
                return tens[n/10] + ' ' + helper(n%10)
            else:
                return lessThan20[n/100] + ' Hundred ' + helper(n%100)
        
        for i in range(len(thousands)):
            if num % 1000 != 0:
                res = helper(num%1000) + thousands[i] + ' ' + res
            num /= 1000
        return res.strip()