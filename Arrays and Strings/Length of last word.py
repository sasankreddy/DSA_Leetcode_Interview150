class Solution(object):
    def lengthOfLastWord(self, s):
        # My approach:
        # - The task is to find the length of the last word in a given string `s`.
        # - A word is defined as a sequence of non-space characters.
        # - Split the string into a list of words using the `split()` method, which automatically removes extra spaces.
        # - Access the last word in the list and return its length.

        # Time complexity:
        # - Splitting the string using `split()` takes O(n), where `n` is the length of the string.
        # - Accessing the last word and finding its length takes O(1).
        # - Overall, the time complexity is O(n).

        l = s.split()  # Split the string into words.
        return len(l[len(l) - 1])  # Return the length of the last word.
        """
        :type s: str
        :rtype: int
        """
