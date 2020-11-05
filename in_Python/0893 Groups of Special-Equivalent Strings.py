class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d = set()
        for a in A:
            odd = []
            even = []
            for i in range(len(a)):
                if i % 2 == 0:
                    even.append(a[i])
                else:
                    odd.append(a[i])
            odd.sort()
            even.sort()
            o = ''.join(odd)
            e = ''.join(even)
            d.add(o+e)
        return len(d)