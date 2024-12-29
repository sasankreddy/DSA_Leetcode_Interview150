from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # My approach: 
        # - The problem requires us to merge two sorted arrays, nums1 and nums2, into a single sorted array in nums1.
        # - We do this by first copying the elements of nums2 into the remaining spaces of nums1.
        # - After the copy operation, we simply sort nums1 to get the final result.
        # Time complexity: O((m + n) log (m + n)) due to the sort operation.
        # Space complexity: O(1) as the merge is done in-place in nums1.
        
        # Copy elements from nums2 into nums1 at the appropriate positions
        for i in range(n):
            nums1[m + i] = nums2[i]

        # Sort the merged array
        nums1.sort()
        """
        Do not return anything, modify nums1 in-place instead.
        """
