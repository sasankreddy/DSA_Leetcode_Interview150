from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # My approach:
        # - The problem requires us to remove all occurrences of a specific value 'val' from the array nums.
        # - We use a two-pointer approach where we iterate over the array using an index i.
        # - If the current element is not equal to 'val', we place it at the 'ind' position and increment 'ind'.
        # - At the end of the iteration, 'ind' will represent the length of the array with 'val' removed.
        # Time complexity: O(n), where n is the length of the array. We traverse the array once.
        # Space complexity: O(1), as we are modifying the array in-place without using extra space.
        
        ind = 0
        # Iterate over each element of the array
        for i in range(len(nums)):
            if nums[i] != val:  # If the element is not equal to 'val', keep it in the array
                nums[ind] = nums[i]
                ind += 1  # Increment the index for the next valid element
        
        # Return the new length of the array after removing 'val'
        return ind
