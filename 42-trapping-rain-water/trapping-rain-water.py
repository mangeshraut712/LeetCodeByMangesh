from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        total_water = 0
        
        # Compute left_max for each position
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        
        # Compute right_max for each position
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        
        # Compute water trapped at each position
        for i in range(n):
            water_at_i = min(left_max[i], right_max[i]) - height[i]
            if water_at_i > 0:
                total_water += water_at_i
        
        return total_water