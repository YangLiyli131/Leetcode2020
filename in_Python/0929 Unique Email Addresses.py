class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        temp = []
        for w in emails:
            t = w.split('@')
            s1 = t[0]
            s2 = t[1]
            new_s1 = ""
            for i in range(len(s1)):
                if s1[i] == '.':
                    continue
                elif s1[i] == '+':
                    break
                else:
                    new_s1 += s1[i]
            new_s = new_s1 + '@' + s2
            if new_s not in temp:
                temp.append(new_s)
        return len(temp)
        