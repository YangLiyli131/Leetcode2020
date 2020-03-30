class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        temp = []
        for w in words:
            s = ""
            for i in range(len(w)):
                s += dic[ord(w[i]) - ord('a')]
            if s not in temp:
                temp.append(s)
        return len(temp)
                
            