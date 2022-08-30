from collections import Counter


class MinimumWindowSubString(object):
    @staticmethod
    def minWindow(S, T):
        if not S or not T:
            return ""
        # dictionary keep unique characters
        dict_T = Counter(T)
        left, right, start, count, min_len = 0, 0, 0, 0, float('inf')
        print(min_len)
        window = {}

        while right < len(S):
            ch = S[right]
            right += 1
            if ch in dict_T:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == dict_T[ch]:
                    count += 1
            while count == len(dict_T):
                del_ch = S[left]
                if right - left < min_len:
                    min_len = right - left
                    start = left
                left += 1
                if del_ch in dict_T:
                    if dict_T[del_ch] == window[del_ch]:
                        count -= 1
                    window[del_ch] -= 1
        return "" if min_len == float('inf') else S[start:start + min_len]


res = MinimumWindowSubString.minWindow("ADOBECODEBANC", "ABC")
print(res)
