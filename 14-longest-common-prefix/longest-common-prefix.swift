import Foundation // Not strictly needed

class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        guard let firstStr = strs.first, !firstStr.isEmpty else {
            return ""
        }
        
        if strs.count == 1 {
            return firstStr
        }

        var prefix = ""
        let firstStrChars = Array(firstStr)

        for i in 0..<firstStrChars.count {
            let charToMatch = firstStrChars[i]
            
            for j in 1..<strs.count {
                let currentStrChars = Array(strs[j])
                if i >= currentStrChars.count || currentStrChars[i] != charToMatch {
                    return prefix
                }
            }
            prefix.append(charToMatch)
        }
        
        return prefix
    }
}
