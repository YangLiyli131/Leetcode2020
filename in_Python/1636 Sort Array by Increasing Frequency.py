class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == None or len(nums) == 0:
            return []
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        counter = {}
        for k in count:
            val = count[k]
            if val not in counter:
                counter[val] = [k]
            else:
                counter[val].append(k)
        v = counter.keys()
        v.sort()
        res = []
        for vi in v:
            cur = counter[vi]
            if len(cur) > 1:
                cur.sort(reverse = True)
            for x in cur:
                y = vi
                while y != 0:
                    y-= 1
                    res.append(x)
        return res
                