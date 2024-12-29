from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # My approach:
        # - The task is to find all unique triplets in the array `nums` that sum up to 0.
        # - We start by dividing the numbers into three categories: positive numbers (p), negative numbers (n), and zeros (z).
        # - We store the negative and positive numbers in sets to enable faster lookups while checking for triplets.
        # - First, if there are zeros in the array, we check if there's a pair of positive and negative numbers that sum to zero and add the corresponding triplet.
        # - If there are at least three zeros, we add the triplet (0, 0, 0) to the result.
        # - Next, we check all pairs of negative numbers and positive numbers, and if their sum has the opposite sign, we add the triplet to the result.
        # - To ensure uniqueness, we use a set to store the triplets, as it will automatically discard duplicate entries.

        # Time complexity:
        # - The time complexity is O(n^2), where n is the length of the `nums` array.
        #   We loop through each pair of elements in `n` and `p`, and for each pair, we check if a matching target exists in the other set.
        # - Sorting is not required, as we are using the set data structure to ensure uniqueness.

        res = set()  # Store unique triplets.
        n = []  # List to store negative numbers.
        p = []  # List to store positive numbers.
        z = []  # List to store zeros.

        # Split the numbers into negative, positive, and zero categories.
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        # Convert lists of negative and positive numbers into sets for faster lookup.
        N, P = set(n), set(p)

        # If there are zeros, check if there's a pair of positive and negative numbers that sum to zero.
        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))

        # If there are at least three zeros, add the triplet (0, 0, 0) to the result.
        if len(z) >= 3:
            res.add((0, 0, 0))

        # Check pairs of negative numbers for a valid triplet with a positive number.
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -(n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # Check pairs of positive numbers for a valid triplet with a negative number.
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -(p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        # Return the list of unique triplets.
        return list(res)
