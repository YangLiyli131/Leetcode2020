class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence) + ' '
        pointer = 0
        N = len(s)
        for row in range(rows):
            pointer += cols - 1
            if s[pointer % N] == ' ':
                pointer += 1
            elif s[(pointer+1) % N] == ' ':
                pointer += 2
            else:
                while pointer > 0 and s[(pointer-1) % N] != ' ':
                    pointer -= 1
        return pointer / N
        

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        word_indx = 0
        N = len(sentence)
        all_length = []
        for x in sentence:
            all_length.append(len(x))
        row = 0
        while row < rows:
            remain = cols
            while remain >= all_length[word_indx % N]:
                remain -= all_length[word_indx % N] + 1
                word_indx += 1
            row += 1
        return word_indx / N