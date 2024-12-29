from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # My approach:
        # - I use a set to store the elements of the array for efficient O(1) lookup.
        # - For each number, if it's the start of a potential sequence (i.e., number-1 is not in the set),
        #   I count how long the sequence can be by incrementing the number and checking for the next number in the sequence.
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)

        return max_length
