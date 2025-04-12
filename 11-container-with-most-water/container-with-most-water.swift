import Foundation // For max, min - though often implicitly available

class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var left = 0
        var right = height.count - 1
        var max_area = 0

        while left < right {
            let current_height = min(height[left], height[right])
            let current_width = right - left
            let current_area = current_height * current_width
            max_area = max(max_area, current_area)

            if height[left] < height[right] {
                left += 1
            } else {
                right -= 1
            }
        }
        
        return max_area
    }
}
