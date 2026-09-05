class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}
        required = len(need)
        formed = 0

        left = 0
        min_len = float("inf")
        best_start = 0

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_len = curr_len
                    best_start = left

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return "" if min_len == float("inf") else s[best_start : best_start + min_len]