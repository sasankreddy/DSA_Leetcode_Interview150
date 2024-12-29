class Solution:
    def majorityElement(self, nums):
        # My approach:
        # - We can use sorting to find the majority element.
        # - After sorting, the majority element will always appear at the middle of the array because it occurs more than n/2 times.
        # - Therefore, the element at index len(nums) // 2 will be the majority element.
        
        nums.sort()  # Sort the array
        
        # Time Complexity: O(n log n) for sorting the array using nums.sort()
        
        n1 = len(nums) // 2  # Calculate the middle index
        return nums[n1]  # The majority element will be at the middle index
