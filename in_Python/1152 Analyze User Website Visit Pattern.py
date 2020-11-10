class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        users = {}
        for i in range(len(username)):
            a = username[i]
            w = website[i]
            t = timestamp[i]
            if a not in users:
                users[a] = [[t,w]]
            else:
                users[a].append([t,w])
        for k in users:
            row = users[k]
            newrow = []
            row = sorted(row, key = lambda x : x[0])
            for x in row:
                newrow.append(x[1])
            users[k] = newrow
        sequence = {}
        uservisits = {}
        for k in users:
            row = users[k]
            newrow = set()
            for i in range(len(row)):
                for j in range(i+1, len(row)):
                    for p in range(j+1, len(row)):
                        tmp = (row[i],row[j],row[p])
                        newrow.add(tmp)
            uservisits[k] = newrow
        for k in uservisits:
            for x in uservisits[k]:
                if x not in sequence:
                    sequence[x] = 1
                else:
                    sequence[x] += 1
        maxseq = []
        count = -1
        for key in sequence:
            if sequence[key] > count:
                count = sequence[key]
                maxseq = [key]
            elif sequence[key] == count:
                maxseq.append(key)
        maxseq.sort()
        return list(maxseq[0])