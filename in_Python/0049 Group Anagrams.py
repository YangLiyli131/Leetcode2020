class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in dict:
                dict[ss].append(s)
            else:
                newList = []
                newList.append(s)
                dict[ss] = newList
        res = []
        for k in dict: res.append(dict[k])
        return res