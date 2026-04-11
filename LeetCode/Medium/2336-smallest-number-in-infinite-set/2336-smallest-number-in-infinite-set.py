import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap_set = set()
        for i in range(1, 1001):
            self.heap_set.add(i)
        
        self.heap = list(self.heap_set)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.heap)
        self.heap_set.remove(smallest)
        
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.heap_set:
            self.heap_set.add(num)
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)