class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        dict_target = {}
        for c in list(chars):
            if c not in dict_target:
                dict_target[c] = 1
            else:
                dict_target[c] += 1
                                
        for w in words:
            dict = {}
            flag = False
            for i in list(w):
                if i not in dict_target:
                    flag = True
                    break
                else:
                    if i not in dict:
                        dict[i] = 1
                    else:
                        dict[i] += 1
            if flag:
                continue
            for k in dict:
                if dict[k] > dict_target[k]:
                    flag = True
                    break
            if flag:
                continue
            else:
                res += len(w)
        return res
                
        