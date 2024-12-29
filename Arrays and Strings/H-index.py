from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # My approach:
        # - The h-index is the highest number 'h' such that the researcher has at least 'h' papers 
        #   with 'h' or more citations.
        # - To find the h-index:
        #   1. First, sort the citations in descending order, so we can check the condition for h-index.
        #   2. Traverse through the sorted citations:
        #      - For each paper at index 'i', we check if the number of citations is less than 'i+1'.
        #      - If this is true, it means that the h-index is 'i' because we can have 'i' papers with 
        #        at least 'i' citations.
        #   3. If no such condition is found during the loop, the h-index is the length of the list.
        # Time complexity: O(n log n) due to sorting.
        # Space complexity: O(1) because we are modifying the list in-place without using extra space.
        
        if len(citations) == 1:
            return 0 if citations[0] == 0 else 1  # Handle case where there is only one paper
        
        citations.sort(reverse=True)  # Sort the citations in descending order
        
        # Traverse the sorted citations to find the h-index
        for i in range(len(citations)):
            if citations[i] < i + 1:  # If citations[i] is less than (i + 1), return i
                return i
        
        return len(citations)  # If no condition is met, the h-index is the total number of papers
