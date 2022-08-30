# Given a non-empty string s and a dictionary wordDict containing
# a list of non-empty words, add spaces in s to construct a sentence
# where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# sentences(i) returns a list of all sentences that can be built from the suffix s[i:].


# python 中的and从左到右计算表达式，若所有值均为真，则返回最后一个值，若存在假，返回第一个假值。
class WordBreak2(object):
    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}

        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i+1, len(s)+1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)


lists = [i+j for i in range(1,10) if i >= 3 for j in range(1,10)]
# list2 = [str[i:tail] + (tail and ' ' + tail) for i in range(0, len(str)) if i >1 for tail in range(1,5)]
listEmpty = [1]
print (listEmpty and 3 + 1)
