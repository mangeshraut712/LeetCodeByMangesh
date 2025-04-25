from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, find_first):
            low = 0
            high = len(nums) - 1
            result_pos = -1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    result_pos = mid
                    if find_first:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return result_pos

        start_index = binary_search(nums, target, True)
        end_index = binary_search(nums, target, False)

        return [start_index, end_index]