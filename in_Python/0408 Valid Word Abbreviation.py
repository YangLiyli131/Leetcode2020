class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        parts = []
        st = []
        for i in abbr:
            if 'a' <= i <= 'z':
                if len(st) != 0:
                    parts.append(''.join(st))
                    st = []
                parts.append(i)
            else:
                st.append(i)
        if len(st) != 0:
            parts.append(''.join(st))
        i,j = 0,0
        while j < len(parts) and i < len(word):
            if 'a' <= parts[j] <= 'z':
                if word[i] != parts[j]:
                    return False
                i += 1
                j += 1
            else:
                if parts[j][0] == '0':
                    return False
                dis = int(parts[j])
                i += dis
                j += 1
        return i == len(word) and j == len(parts)
            
        