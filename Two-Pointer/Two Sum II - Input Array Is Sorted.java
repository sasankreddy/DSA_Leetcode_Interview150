import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // My approach:
        // - The task is to find two numbers in the array `nums` that add up to the given `target`.
        // - I first sort the array to apply the two-pointer technique.
        // - Initialize two pointers, `i` and `j`, at the start and end of the sorted array, respectively.
        // - If the sum of the numbers at the pointers equals the target, I return the 1-based indices of those numbers.
        // - If the sum is greater than the target, I move the right pointer `j` left to reduce the sum.
        // - If the sum is less than the target, I move the left pointer `i` right to increase the sum.
        // - The two-pointer approach ensures that we efficiently find the pair in one pass through the array.

        // Time complexity:
        // - Sorting the array takes O(n log n), and the while loop takes O(n), where n is the number of elements in `nums`.
        // - So, the overall time complexity is O(n log n).

        // Space complexity:
        // - The space complexity is O(1) because we are using only a few extra variables and no additional data structures.

        int i = 0;  // Left pointer.
        int j = nums.length - 1;  // Right pointer.
        int index1 = 0;  // First index of the pair (1-based).
        int index2 = 0;  // Second index of the pair (1-based).
        
        Arrays.sort(nums);  // Sort the array to apply the two-pointer technique.

        while (i < j) {
            if (nums[i] + nums[j] == target) {  // If the sum of the two numbers equals the target.
                index1 = i + 1;  // Store the 1-based index.
                index2 = j + 1;  // Store the 1-based index.
                return new int[]{index1, index2};  // Return the result.
            }
            if (nums[i] + nums[j] > target) {  // If the sum is too large, move the right pointer left.
                j--;
            } else {  // If the sum is too small, move the left pointer right.
                i++;
            }
        }

        return new int[]{index1, index2};  // Return the indices if no solution found.
    }
}
