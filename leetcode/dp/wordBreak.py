class wordBreak:
    def wordBreak(self, s, wordDict):
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w)==-1):
                    d[i] = True

        return d[-1]
# ok[i] tells whether s[:i] can be built.
    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]