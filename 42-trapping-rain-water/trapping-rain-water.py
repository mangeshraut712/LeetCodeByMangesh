from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total_water = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                h = min(height[left], height[i]) - height[bottom]
                w = i - left - 1
                total_water += h * w
            stack.append(i)
        
        return total_water