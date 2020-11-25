# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        def getHost(x):
            idx = -1
            for i in range(7,len(x)):
                if x[i] == '/':
                    idx = i
                    break
            if idx == -1:
                return x
            return x[:idx]
        
        host = getHost(startUrl)
        res = []
        seen = set()
        seen.add(startUrl)
        q = [startUrl]
        while q:
            h = q.pop(0)
            for nex in htmlParser.getUrls(h):
                if nex.startswith(host) and nex not in seen:
                    seen.add(nex)
                    q.append(nex)
            res.append(h)
        return res
                