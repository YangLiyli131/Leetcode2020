class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        dict = {}
        l1 = ['q','w','e','r','t','y','u','i','o','p']
        l2 = ['a','s','d','f','g','h','j','k','l']
        l3 = ['z','x','c','v','b','n','m']
        for x in l1:
            dict[x] = 1
        for x in l2:
            dict[x] = 2
        for x in l3:
            dict[x] = 3
        for w in words:
            flag = False
            temp = []
            for i in list(w):
                if dict[i.lower()] not in temp:
                    temp.append(dict[i.lower()])
                if len(temp) == 2:
                    flag = True
                    break
            if not flag:
                res.append(w)
        return res