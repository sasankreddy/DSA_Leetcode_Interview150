from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # My approach:
        # - The task is to find the maximum area of water that can be trapped between two lines on the x-axis,
        #   where the heights of the lines are given in the list `height`.
        # - The area between two lines is calculated as `min(height[i], height[j]) * (j - i)`,
        #   where `i` and `j` are the indices of the two lines.
        # - To maximize the area, we start with two pointers: one at the beginning (i = 0) and the other at the end (j = len(height) - 1).
        # - In each step, calculate the area between the lines at indices `i` and `j`, and update the result `res` if the area is larger.
        # - Move the pointer pointing to the smaller height towards the other pointer in hopes of finding a taller line
        #   that could potentially increase the area.
        # - Repeat this process until the two pointers meet.

        # Time complexity:
        # - We iterate through the list with two pointers, so the time complexity is O(n),
        #   where n is the length of the `height` list.

        # Space complexity:
        # - The space complexity is O(1), as we are using only a few extra variables and no additional data structures.

        i = 0  # Left pointer.
        j = len(height) - 1  # Right pointer.
        res = 0  # Variable to store the maximum area.

        while i < j:  # Continue until the two pointers meet.
            # Calculate the area and update `res` if it's larger than the current max area.
            res = max(res, min(height[i], height[j]) * (j - i))
            # Move the pointer pointing to the shorter height.
            if height[i] < height[j]:
                i += 1  # Move left pointer.
            else:
                j -= 1  # Move right pointer.

        return res  # Return the maximum area found.
