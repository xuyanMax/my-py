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
                if w == s[i - len(w) + 1:i + 1] and (d[i - len(w)] or i - len(w) == -1):
                    d[i] = True
        return d[-1]

    wordDict = []
    # found = False
    found = False

    # O(2^n * n^2)
    def wordBreak_dfs(self, s, words):
        def backtrace(s: str, pos: int, path):
            if wordBreak.found:
                return
            if pos == len(s):
                wordBreak.found = True
                return
            for l in range(1, len(s) - pos + 1):
                if s[pos:pos + l] in wordBreak.wordDict:
                    print(" " * (pos), pos, s[pos:pos + l], s[pos:pos + l] in wordBreak.wordDict)
                    path.append(s[pos:pos + l])
                    backtrace(s, pos + l, path)
                    path.pop()
            print(" " * pos, track_path)

        wordBreak.wordDict = words
        track_path = []
        backtrace(s, 0, track_path)
        print(track_path)
        return wordBreak.found

    # def wordBreak_dp(self, s, word):
    # def dp(s:str:, pos:int)

    def wordBreak_dp(self, s, wordDict: list[int]):
        # dp(s,i) 定义s[i...]是否能够拼出

        def dp(s, i, wordDict: set[int], memo: list[int]):
            # base case
            if i == len(s):
                return True
            if memo[i] != 1:
                return True if memo[i] == 1 else False

            for l in range(1, len(s) - i + 1):
                # 返回 s[i:i+l), right bound exclusive
                prefix = s[i:i + l]
                print(prefix)
                if prefix in wordDict:
                    # 找到一个匹配的s[i+l..)
                    # 只要s[i+l..]可以被拼出，那么s[i..)也可以
                    subProb = dp(s, i + l, wordDict)
                    if subProb:
                        memo[i] = 1
                        return True
            # 全部尝试后无有效匹配，在此返回False
            memo[i] = 0
            return False

        # 备忘录，-1代表未计算, 0 代表s[i..]没有凑出，1代表组合成功
        memo = [-1] * len(s)
        wordDict = set(wordDict)
        print(wordDict)
        return dp(s, 0, wordDict, memo)


s = "aaab"
wordDict = ['a', 'aa', 'va', 'ab']
wordBreak = wordBreak()
# print(wordBreak.wordBreak_dfs(s, wordDict))

print(wordBreak.wordBreak_dp(s, wordDict))
