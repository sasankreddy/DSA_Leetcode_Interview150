class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # My approach:
        # - The task is to find the length of the longest substring in `s` without repeating characters.
        # - We check every possible substring of `s` by iterating through the string.
        # - For each substring, we convert it to a set, which removes any duplicate characters, 
        #   and check if the length of the set equals the length of the substring. 
        # - If they are equal, it means the substring has all unique characters, and we update the maximum length found so far.

        # Time complexity:
        # - The time complexity is O(n^3) because we generate all substrings (O(n^2)) and convert each substring to a set (O(n)).
        #   This results in a cubic time complexity, which is inefficient for larger strings.
        
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        
        m = 0  # Variable to store the length of the longest substring without repeating characters.
        
        # Iterate through all possible substrings of s.
        for i in range(len(s)):
            for j in range(i, len(s)):
                s1 = s[i:j + 1]  # Extract the substring from i to j.
                if len(s1) == len(set(s1)):  # Check if all characters in the substring are unique.
                    if len(s1) > m:
                        m = len(s1)  # Update the maximum length.
        
        return m  # Return the length of the longest substring found.
