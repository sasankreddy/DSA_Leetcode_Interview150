class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # My approach:
        # - The task is to check if string 's' is a subsequence of string 't'.
        # - A subsequence means that the characters of 's' appear in 't' in the same order, but not necessarily consecutively.
        # - Use two pointers (`i` for 's' and `j` for 't') to traverse both strings.
        # - Compare the characters at both pointers. If they match, move both pointers forward.
        # - If the character at pointer `i` doesn't match `j`, move `j` forward to check the next character of 't'.
        # - If pointer `i` reaches the end of 's', it means all characters of 's' have been found in order in 't'.
        # - If pointer `i` does not reach the end of 's' after traversing 't', return False.

        # Time complexity:
        # - We traverse both strings, resulting in (O(n + m)), where (n) is the length of 's' and (m) is the length of 't'.

        # Space complexity:
        # - The space complexity is (O(1) as we are only using a few pointers and no extra space.

        i = 0  # Pointer for string 's'.
        j = 0  # Pointer for string 't'.

        # Traverse both strings until one of them is fully checked.
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move both pointers.
                i += 1
            # Always move pointer `j` in `t`.
            j += 1

        # If `i` has reached the end of `s`, it means all characters of `s` have been found in `t` in order.
        return i == len(s)
