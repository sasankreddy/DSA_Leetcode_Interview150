from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # My approach:
        # - The goal is to find the minimal length of a contiguous subarray whose sum is greater than or equal to the target.
        # - We use the sliding window technique, where the window expands as long as the sum is less than the target, 
        #   and it shrinks when the sum becomes greater than or equal to the target.
        # - We keep track of the minimal window length during this process.
        # - If no such subarray is found, we return 0.

        # Time complexity:
        # - The time complexity is O(n), where n is the length of the `nums` array. 
        #   We iterate over the array once with two pointers (`i` and `j`) moving independently within the loop.

        i = 0  # Pointer to the start of the window.
        s = 0  # Running sum of the current window.
        mini = float('inf')  # Variable to store the minimum length of the subarray.
        
        # Iterate through the array with j being the end of the sliding window.
        for j in range(len(nums)):
            s += nums[j]  # Add the current number to the running sum.
            
            # When the running sum is greater than or equal to the target, try to shrink the window.
            while s >= target:
                mini = min(mini, j - i + 1)  # Update the minimum length.
                s -= nums[i]  # Shrink the window from the left.
                i += 1  # Move the left pointer forward.
        
        # If no subarray was found, return 0; otherwise, return the minimum length found.
        return mini if mini != float('inf') else 0
