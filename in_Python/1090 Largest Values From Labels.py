class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        q = []
        for i in range(len(values)):
            v = values[i]
            l = labels[i]
            q.append([v,l])
        q = sorted(q, key = lambda x : x[0], reverse = True)
        counter = {}
        r = 0
        t = 0
        for i in range(len(q)):
            v, l = q[i]
            if l not in counter:
                r += v
                counter[l] = 1
                t += 1
            else:
                if counter[l] < use_limit:
                    r += v
                    counter[l] += 1
                    t += 1
            if t == num_wanted:
                break
        return r