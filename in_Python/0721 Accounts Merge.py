class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        v = [0] * len(accounts)
        emailmap = {}
        for i in range(len(accounts)):
            row = accounts[i]
            for j in range(1, len(row)):
                e = row[j]
                if e not in emailmap:
                    t = [i]
                    emailmap[e] = t
                else:
                    t = emailmap[e]
                    t.append(i)
                    emailmap[e] = t        
        res = []
        def dfs(i, emails):
            if v[i] == 1:
                return
            v[i] = 1
            for e in range(1, len(accounts[i])):
                emails.add(accounts[i][e])
                for nextn in emailmap[accounts[i][e]]:
                    dfs(nextn, emails)     
        for i, acc in enumerate(accounts):
            if v[i] == 1:
                continue
            name = acc[0]
            em = set()
            dfs(i, em)
            res.append([name] + sorted(em))
        return res
            
                    
            
        