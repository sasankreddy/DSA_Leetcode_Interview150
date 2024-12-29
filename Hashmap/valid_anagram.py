class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # My approach:
        # - The goal is to check if two strings s and t are anagrams, meaning that they have the same characters with the same frequencies.
        # - I define a helper function `freq(s)` that returns the frequency count of characters in string `s`:
        #     - I initialize an array `ans` of size 26 (since there are 26 lowercase English letters).
        #     - For each character `c` in the string `s`, I update the frequency count in the array using the formula `ord(c) - ord('a')`.
        # - After computing the frequency count for both strings, I simply compare the frequency arrays. If they are the same, the strings are anagrams.
        
        # Time complexity:
        # - The time complexity is O(n), where n is the length of the strings s and t. 
        # - We iterate through each string once to calculate the frequencies, and the comparison of the two frequency arrays is done in constant time (O(1)) since the array size is fixed (26).

        def freq(s):
            ans = [0] * 26
            for c in s:
                ans[ord(c) - ord('a')] += 1
            return ans

        return freq(s) == freq(t)
