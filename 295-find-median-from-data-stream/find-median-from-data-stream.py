import heapq

class MedianFinder:
    def __init__(self):
        self.small_half_max_heap = []  # Max heap for smaller half
        self.large_half_min_heap = []  # Min heap for larger half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_half_max_heap, -num)
        if (self.small_half_max_heap and self.large_half_min_heap and
                (-self.small_half_max_heap[0]) > self.large_half_min_heap[0]):
            val = -heapq.heappop(self.small_half_max_heap)
            heapq.heappush(self.large_half_min_heap, val)
        if len(self.small_half_max_heap) > len(self.large_half_min_heap) + 1:
            val = -heapq.heappop(self.small_half_max_heap)
            heapq.heappush(self.large_half_min_heap, val)
        elif len(self.large_half_min_heap) > len(self.small_half_max_heap):
            val = heapq.heappop(self.large_half_min_heap)
            heapq.heappush(self.small_half_max_heap, -val)

    def findMedian(self) -> float:
        if len(self.small_half_max_heap) > len(self.large_half_min_heap):
            return float(-self.small_half_max_heap[0])
        return (-self.small_half_max_heap[0] + self.large_half_min_heap[0]) / 2.0