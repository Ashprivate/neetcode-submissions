class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
         
        # Convert to negative values to simulate a max-heap
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            # Extract the two heaviest stones
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)

            # If their weights differ, insert the remaining stone
            if first != second:
                remaining = first - second
                heapq.heappush(maxHeap, -remaining)

        # Return the remaining stone's weight, or 0
        return -maxHeap[0] if maxHeap else 0