from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # My approach:
        # - The task is to remove duplicates from the sorted array 'nums'.
        # - We use a two-pointer technique: one pointer keeps track of the next position to replace with a unique element.
        # - We iterate through the array, and when we encounter a new unique element, we move the 'replace' pointer
        #   to the next available position and replace the value at that position with the new unique element.
        # - At the end, the array will contain only the unique elements in the first 'replace' positions.
        # Time complexity: O(n), where n is the length of the array. We traverse the array once.
        # Space complexity: O(1), as we are modifying the array in-place without using extra space.
        
        replace = 1  # Pointer for the position to place the next unique element
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous element, it's a unique element
            if nums[i-1] != nums[i]:
                nums[replace] = nums[i]  # Place the unique element at the 'replace' position
                replace += 1  # Increment the 'replace' pointer to the next position
        
        # Return the length of the array with unique elements
        return replace
