class Solution:
    def strStr(self, h: str, n: str) -> int:
        # My approach:
        # - The task is to find the index of the first occurrence of string `n` in string `h`. If `n` is not found, return -1.
        # - Handle special cases: if `n` is of length 1 or `h` is equal to `n`.
        # - Use a sliding window approach to compare substrings of length `len(n)` in `h` with `n`.
        # - If a match is found, return the starting index of the substring; otherwise, return -1.

        # Time complexity:
        # - Outer loop runs \(O(m - n + 1)\), where \(m = \text{len}(h)\) and \(n = \text{len}(n)\).
        # - Substring comparison takes \(O(n)\) for each iteration.
        # - Overall, the time complexity is \(O(m \times n)\) in the worst case.

        # Space complexity:
        # - The space complexity is \(O(1)\) as no extra data structures are used apart from variables.

        if len(n) == 1:  # Special case: `n` is a single character.
            for i in range(len(h)):
                if h[i] == n:  # Compare each character in `h` with `n`.
                    return i

        if h == n:  # Special case: `h` and `n` are identical.
            return 0

        # Sliding window approach to find `n` in `h`.
        for i in range(len(h) - len(n) + 1):
            if h[i:i + len(n)] == n:  # Compare substring of length `len(n)` with `n`.
                return i

        return -1  # If no match is found.
