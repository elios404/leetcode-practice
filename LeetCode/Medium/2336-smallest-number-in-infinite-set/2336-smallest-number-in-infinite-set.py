import heapq

class SmallestInfiniteSet:
    def __init__(self):
        # The pointer representing the lowest untouched number in the infinite set
        self.current_min = 1
        
        # Only stores numbers that were explicitly added back (out-of-sequence)
        self.added_back_heap = []
        self.added_back_set = set() # For O(1) duplicate checking

    def popSmallest(self) -> int:
        # Priority 1: Check if any smaller numbers re-entered the pool
        if self.added_back_heap:
            smallest = heapq.heappop(self.added_back_heap)
            self.added_back_set.remove(smallest)
            return smallest
        
        # Priority 2: Standard continuous sequence
        smallest = self.current_min
        self.current_min += 1
        return smallest

    def addBack(self, num: int) -> None:
        # We only care if the number is actually smaller than our pointer
        # and not already sitting in our waiting pool.
        if num < self.current_min and num not in self.added_back_set:
            self.added_back_set.add(num)
            heapq.heappush(self.added_back_heap, num)