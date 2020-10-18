class Codec:
    code = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    d = {}
    idx = 1
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        re = ''
        self.d[self.idx] = longUrl
        n = self.idx
        while n:
            re += self.code[n % 62]
            n /= 62
        self.idx += 1
        return re
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        i = 0
        for x in shortUrl:
            if 'a' <= x <= 'z':
                i = i * 62 + ord(x) - ord('a') 
            elif 'A' <= x <= 'Z':
                i = i * 62 + ord(x) - ord('A') + 26
            else:
                i = i * 62 + ord(x) - ord(0) + 52
        return self.d[i]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))