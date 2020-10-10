class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        d = {'&quot;': '"',
            '&apos;': '\'',
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/'}
        res = ""
        i = 0
        while i < len(text):
            if text[i] != '&':
                res += text[i]
                i += 1
            else:
                j = i+1
                while j < len(text) and text[j] != ';':
                    j += 1
                key = text[i:j+1]
                if key in d:
                    res += d[key]
                else:
                    res += key
                i = j + 1
        return res