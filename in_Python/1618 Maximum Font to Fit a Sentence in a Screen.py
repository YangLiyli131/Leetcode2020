# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution(object):
    def maxFont(self, text, w, h, fonts, fontInfo):
        """
        :type text: str
        :type w: int
        :type h: int
        :type fonts: List[int]
        :type fontInfo: FontInfo
        :rtype: int
        """
        i,j = 0, len(fonts)-1
        
        def check(tx, fi, fs, w, h):
            curw = 0
            for x in tx:
                if fi.getHeight(fs) > h:
                    return False
                curw += fi.getWidth(fs,x) 
                if curw > w:
                    return False
            return True
        
        while i+1 < j:
            m = i + (j-i) / 2
            if check(text, fontInfo, fonts[m], w, h):
                i = m
            else:
                j = m-1
        if check(text, fontInfo, fonts[j], w, h):
            return fonts[j]
        if check(text, fontInfo, fonts[i], w, h):
            return fonts[i]
        return -1