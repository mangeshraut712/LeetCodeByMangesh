from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        if n < 4:
            return []

        for i in range(n - 3):
            # Skip duplicate for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early exit optimization 1 (Optional but can help)
            # if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
            #     break 
            # Early exit optimization 2 (Optional but can help)
            # if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
            #     continue

            for j in range(i + 1, n - 2):
                # Skip duplicate for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Early exit optimization 3 (Optional but can help)
                # if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                #     break
                # Early exit optimization 4 (Optional but can help)
                # if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                #     continue

                left, right = j + 1, n - 1
                required_sum = target - nums[i] - nums[j]

                while left < right:
                    current_two_sum = nums[left] + nums[right]

                    if current_two_sum == required_sum:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates for the third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_two_sum < required_sum:
                        left += 1
                    else: # current_two_sum > required_sum
                        right -= 1
                        
        return result
