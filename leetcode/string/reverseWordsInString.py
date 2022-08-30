class ReverseWordsInString:
    # Input: s = "  Bob    Loves  Alice   "
    # Output: "Alice Loves Bob"
    def sol(self, s):
        return " ".join(s.strip().split()[::-1])

    def sol1(self, s):
        return " ".join(reversed(s.split()))

