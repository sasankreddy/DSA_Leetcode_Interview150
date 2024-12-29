from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # My approach:
        # - The task is to find the product of all elements except the current element at each index.
        # - We solve this without using division, and in O(n) time with O(1) space.
        # - We compute two products:
        #    1. Prefix product: Product of all elements before the current index.
        #    2. Postfix product: Product of all elements after the current index.
        # - We store the result in the 'result' list and update it with the prefix and postfix products.
        
        n = len(nums)  # Get the length of the input list.
        
        # Initialize the prefix_product and postfix_product.
        prefix_product = 1
        postfix_product = 1
        
        # Initialize the result list with zeros.
        result = [0] * n
        
        # Calculate the prefix products and store them in the result array.
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]  # Update prefix_product for the next iteration.
        
        # Calculate the postfix products and update the result array.
        for i in range(n - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]  # Update postfix_product for the next iteration.
        
        return result
