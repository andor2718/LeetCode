# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window_substring = ''
        if len(t) > len(s):  # Sanity check.
            return min_window_substring
        # Preprocess t, find the frequency of every character in it.
        t_char_freqs = dict()
        for char in t:
            t_char_freqs[char] = t_char_freqs.get(char, 0) + 1
        # Use a sliding window that can stretch and shrink as needed.
        left, right = 0, len(t) - 1
        # Initialize char frequencies of the window, count covered characters.
        # We say char is covered if it occurs in t, and it's frequency
        # within the window is >= t_char_freqs[char].
        window_char_freqs = dict()
        covered_chars = 0
        for idx in range(left, right + 1):
            char = s[idx]
            if char in t_char_freqs:
                window_char_freqs[char] = window_char_freqs.get(char, 0) + 1
                if window_char_freqs[char] == t_char_freqs[char]:
                    covered_chars += 1
        # The current window is said to be good if every character in t
        # is covered by the window. If the window is good after the
        # initialization, we can be sure we'll find no smaller window with
        # this property, as the current width of the window equals len(t).
        if covered_chars == len(t_char_freqs):
            min_window_substring = s[left: right + 1]
            return min_window_substring
        # Move with left and right pointers to the right, as long
        # as we have a chance to improve on the min_window_substring.
        while left < len(s) - len(t):
            if right == len(s) - 1 and covered_chars != len(t_char_freqs):
                # We can only shrink, so if the current window
                # is not good, there's no way to change that.
                break
            if covered_chars == len(t_char_freqs):
                # Current window is good, pop the leftmost char.
                curr_char = s[left]
                if curr_char in t_char_freqs:
                    if window_char_freqs[curr_char] == t_char_freqs[curr_char]:
                        covered_chars -= 1
                    window_char_freqs[curr_char] -= 1
                left += 1
            else:
                # Current window is not good, include the
                # next yet not included char on the right.
                right += 1
                curr_char = s[right]
                if curr_char in t_char_freqs:
                    curr_freq = window_char_freqs.get(curr_char, 0) + 1
                    window_char_freqs[curr_char] = curr_freq
                    if window_char_freqs[curr_char] == t_char_freqs[curr_char]:
                        covered_chars += 1
            # Check if current window is good.
            if covered_chars == len(t_char_freqs):
                min_len, curr_len = len(min_window_substring), right - left + 1
                if min_window_substring == '' or min_len > curr_len:
                    # Current window isn't just good, it's the slimmest so far.
                    min_window_substring = s[left: right + 1]
                    if curr_len == len(t):
                        break  # This is the best window, hands down.
        return min_window_substring
