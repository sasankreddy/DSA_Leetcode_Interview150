class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # My approach:
        # - I use a dictionary `d` to store the most recent index of each number.
        # - As I iterate over the array, for each number, I check if it has been encountered before.
        # - If it has, I check if the absolute difference between the current index and the stored index is less than or equal to k.
        # - If so, I return True because there is a nearby duplicate.
        # - Otherwise, I update the dictionary with the current index of the number.
        # - If no duplicates are found that satisfy the condition, I return False.

        d = dict()
        for i in range(len(nums)):
            if nums[i] in d and abs(d[nums[i]] - i) <= k:
                return True
            d[nums[i]] = i
        return False
