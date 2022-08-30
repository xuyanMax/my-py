class wordBreak(object):
    def wordBreak(self, s, words):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False] * len(s)
        for i in range(len(s)):
            for w in words:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]