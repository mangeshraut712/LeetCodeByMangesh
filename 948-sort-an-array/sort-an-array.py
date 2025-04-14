import math
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Helper function to maintain the max heap property for a subtree rooted at index i
        # n is the size of the heap
        def heapify(arr, n, i):
            largest = i  # Initialize largest as root
            left = 2 * i + 1     # left child index
            right = 2 * i + 2    # right child index

            # See if left child exists and is greater than root
            if left < n and arr[left] > arr[largest]:
                largest = left

            # See if right child exists and is greater than the largest so far
            if right < n and arr[right] > arr[largest]:
                largest = right

            # Change root if needed
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # swap
                # Heapify the root of the affected sub-tree
                heapify(arr, n, largest)

        # Build a maxheap. Start from the last non-leaf node.
        # Index of last non-leaf node is n // 2 - 1
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            # Move current root (max element) to the end
            nums[i], nums[0] = nums[0], nums[i]
            # call max heapify on the reduced heap (size i) rooted at 0
            heapify(nums, i, 0)

        return nums

