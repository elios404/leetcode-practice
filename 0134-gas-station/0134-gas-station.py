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
        l = len(gas)
        idx = start = 0
        gas_left = gas[0]
        # maximun two times full scan
        while start < l:
            if (idx-l) == start: #if rotate once
                return start

            gas_left -= cost[idx%l] # move to next gas station
            idx += 1# update idx into next station index

            if gas_left < 0: #if run out of gas
                start = idx
                gas_left = 0

            gas_left += gas[idx%l] # fill gas
        
        return -1