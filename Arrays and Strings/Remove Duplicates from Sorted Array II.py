from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # My approach:
        # - The goal is to allow at most two occurrences of each element in the sorted array.
        # - We use a two-pointer technique where 'i' is the pointer for the position to place the next valid element,
        #   and 'j' is the pointer used to traverse the array.
        # - We check if the current element at index 'j' is different from the element at index 'i-2'.
        # - If it is, we place the element at index 'i' and increment 'i'.
        # - This ensures that no element appears more than twice consecutively in the array.
        # - We return 'i', which gives the new length of the array with at most two duplicates.
        # Time complexity: O(n), where n is the length of the array. We traverse the array once.
        # Space complexity: O(1), as we are modifying the array in-place without using extra space.
        
        if len(nums) <= 2:
            return len(nums)  # If the array length is 2 or less, it's already valid
        
        i = 2  # Pointer to place valid elements in the array
        for j in range(2, len(nums)):  # Start from the third element
            # If the current element is different from the element two positions before it
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]  # Place it at the 'i' position
                i += 1  # Move the 'i' pointer forward
        
        return i  # Return the new length of the array with at most two duplicates
