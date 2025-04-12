import Foundation // Not strictly needed

class Solution {
    func romanToInt(_ s: String) -> Int {
        let romanMap: [Character: Int] = [
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        ]
        
        var total = 0
        var prevValue = 0
        
        for char in s.reversed() {
            guard let currentValue = romanMap[char] else {
                // Should not happen based on constraints, but good practice
                return 0 
            }
            
            if currentValue < prevValue {
                total -= currentValue
            } else {
                total += currentValue
            }
            prevValue = currentValue
        }
        
        return total
    }
}
