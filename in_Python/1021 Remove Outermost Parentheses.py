class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        cummu = 0
        cur_s = ""
        for i in list(S):            
            if i == '(':
                cummu -= 1                
            else:
                cummu += 1
            cur_s += i
            if cummu == 0:
                # now the string is found
                if len(cur_s) != 2:
                    # if len == 2, the string is "()" and no need to add it to result
                    res += cur_s[1:-1] # remove outer paranthese
                cur_s = ""
        return res
        