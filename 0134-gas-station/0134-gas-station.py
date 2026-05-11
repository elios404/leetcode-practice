"""
1. Approach:
    - While searching, if station i'th to i+1'th can't be reached, then there is no available way in what we already seen.
    - So we should start a new route from i+1'th station.
    - % operator is quite slow as I know, wonder is there any other ways implement this.
2. Time Complexity: O(N) - maximum scan two times in gas and cost list. Worst case, route starting from the last station of the lists.
3. Space Complexity : O(1) -  auxiliary const space needed to track idx, start, and gas_left.
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        point = 0
        tank = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank = tank + g - c
            if tank < 0:
                tank = 0
                point = i+1
        
        return point