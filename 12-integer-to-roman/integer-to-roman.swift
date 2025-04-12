import Foundation // Not strictly needed for this logic

class Solution {
    func intToRoman(_ num: Int) -> String {
        let values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        let symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        var result = ""
        var currentNum = num
        
        for i in 0..<values.count {
            let value = values[i]
            let symbol = symbols[i]
            
            while currentNum >= value {
                result += symbol
                currentNum -= value
            }
            if currentNum == 0 {
                 break
            }
        }
        
        return result
    }
}
