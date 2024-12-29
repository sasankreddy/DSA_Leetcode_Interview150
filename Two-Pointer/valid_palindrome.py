class Solution:
    def isPalindrome(self, s: str) -> bool:
        # My approach:
        # - The task is to determine if a given string is a palindrome, considering only alphanumeric characters and ignoring cases.
        # - First, convert the string to lowercase to make it case-insensitive.
        # - Use two pointers (`i` and `j`) starting at the beginning and end of the string.
        # - Skip non-alphanumeric characters using the `isalnum()` method.
        # - Compare characters from both ends; if they don't match, return False.
        # - If the pointers cross without a mismatch, return True.

        # Time complexity:
        # - Each character in the string is visited once, resulting in (O(n)), where (n) is the length of the string.

        # Space complexity:
        # - The space complexity is (O(1)) as we don't use any extra data structures, only a few variables.

        s = s.lower()  # Convert the string to lowercase to ignore case.
        i = 0  # Pointer starting from the beginning of the string.
        j = len(s) - 1  # Pointer starting from the end of the string.

        while i < j:
            # Skip non-alphanumeric characters from the left.
            if not s[i].isalnum():
                i += 1
            # Skip non-alphanumeric characters from the right.
            elif not s[j].isalnum():
                j -= 1
            # Compare the characters at the current pointers.
            elif s[i] != s[j]:
                return False  # If characters don't match, it's not a palindrome.
            else:  # If characters match, move both pointers.
                i += 1
                j -= 1

        return True  # If all characters match, it's a palindrome.
