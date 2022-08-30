# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input: "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".

# Example 2:
# Input: "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".
def longestPalindromeSubseq(self, s):
    d = {}

    def f(s):
        if s not in d:
            maxL = 0
            for c in set(s):
                i, j = s.find(c), s.rfind(c)
                maxL = max(maxL, 1 if i == j else 2 + f(s[i + 1:j]))
            d[s] = maxL
        return d[s]

    return f(s)