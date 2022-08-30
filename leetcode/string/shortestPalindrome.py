class shortestPalindrome(object):
    # Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
    # Find and return the shortest palindrome you can find by performing this transformation.
    #
    # Example 1:
    #
    # Input: "aacecaaa"
    # Output: "aaacecaaa"
    # Example 2:
    #
    # Input: "abcd"
    # Output: "dcbabcd"
    def solution(self, s):
        rev = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(rev[i:]):
                return rev[i:]+s

    def kmp(self, s):
        return 0


    