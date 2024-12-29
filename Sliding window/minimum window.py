from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # My approach:
        # - The task is to find the minimum window in `s` that contains all the characters from `t`.
        # - We use the sliding window technique, where we maintain a window in `s` that expands and contracts dynamically.
        # - We use two pointers, `left` and `right`, to represent the window.
        # - We also maintain counts of characters in `t` (using `t_count`) and the current window (using `window_count`).
        # - As we expand the window by moving the `right` pointer, we check if the window contains all characters from `t`.
        # - If the window is valid (contains all characters from `t`), we try to contract the window by moving the `left` pointer, 
        #   all while tracking the minimum window length and updating the result.

        # Time complexity:
        # - The time complexity is O(n + m), where n is the length of `s` and m is the length of `t`.
        #   - Expanding the window with the `right` pointer takes O(n).
        #   - Contracting the window with the `left` pointer takes O(m) in total since each character in `s` is processed at most twice (once when expanding and once when contracting).
        
        if not t or not s:
            return ""

        t_count = Counter(t)  # Count frequency of each character in t
        required_chars = len(t_count)  # Number of unique characters in t
        window_count = Counter()  # Count frequency of characters in the current window
        
        left, right = 0, 0  # Sliding window pointers
        formed = 0  # Number of characters in the current window that match the required frequency in t
        min_len = float('inf')  # Initialize the minimum length of the window to infinity
        min_window = ""  # To store the minimum window substring

        while right < len(s):
            char = s[right]
            window_count[char] += 1  # Expand the window by including the character at `right`

            # Check if the current character satisfies the required frequency
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1  # Increase the count of formed characters

            # Try to contract the window from the left if it contains all required characters
            while left <= right and formed == required_chars:
                char = s[left]
                
                # Update the result if the current window is smaller than the previous minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                
                window_count[char] -= 1  # Remove the character at `left` from the window
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1  # Reduce the formed count if the character no longer satisfies the required frequency
                
                left += 1  # Contract the window by moving `left` pointer

            right += 1  # Expand the window by moving `right` pointer

        return min_window  # Return the minimum window substring found
