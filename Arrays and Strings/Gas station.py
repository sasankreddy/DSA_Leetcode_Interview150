from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # My approach:
        # - The task is to find the starting gas station index from which the car can complete the circular route.
        # - We track the total gas and cost, and the current gas the car has while traversing.
        # - If at any point, the car doesn't have enough gas to move to the next station, we reset the start index.
        # - If the total gas is less than the total cost, it’s impossible to complete the route, so we return -1.

        total_gas = 0  # Total gas available in all stations.
        total_cost = 0  # Total cost required to travel between stations.
        current_gas = 0  # Current gas the car has while moving.
        start_index = 0  # The index from which we can start the journey.

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]

            # If current gas is negative, reset the start index because the car can't go further from here.
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0

        # If total gas is less than total cost, no solution exists
        return start_index if total_gas >= total_cost else -1
