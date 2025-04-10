import heapq

class MedianFinder:

    def __init__(self):
        self.small_half_max_heap = []  # Stores smaller half, max heap (use negative values)
        self.large_half_min_heap = []  # Stores larger half, min heap

    def addNum(self, num: int) -> None:
        # Add to max_heap (small half), then balance
        heapq.heappush(self.small_half_max_heap, -num)
        
        # Ensure smallest element of large half >= largest element of small half
        if (self.small_half_max_heap and self.large_half_min_heap and
                (-self.small_half_max_heap[0]) > self.large_half_min_heap[0]):
            val_to_move = -heapq.heappop(self.small_half_max_heap)
            heapq.heappush(self.large_half_min_heap, val_to_move)

        # Balance sizes: small_half should have N or N+1 elements, large_half N elements
        if len(self.small_half_max_heap) > len(self.large_half_min_heap) + 1:
            val_to_move = -heapq.heappop(self.small_half_max_heap)
            heapq.heappush(self.large_half_min_heap, val_to_move)
            
        if len(self.large_half_min_heap) > len(self.small_half_max_heap):
            val_to_move = heapq.heappop(self.large_half_min_heap)
            heapq.heappush(self.small_half_max_heap, -val_to_move)

    def findMedian(self) -> float:
        if len(self.small_half_max_heap) > len(self.large_half_min_heap):
            # Odd number of elements, median is top of small_half_max_heap
            return -self.small_half_max_heap[0]
        else:
            # Even number of elements, median is average of tops of both heaps
            small_max = -self.small_half_max_heap[0]
            large_min = self.large_half_min_heap[0]
            return (small_max + large_min) / 2.0