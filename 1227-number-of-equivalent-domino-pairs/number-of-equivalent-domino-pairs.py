class Solution:
    def numEquivDominoPairs(self, dominoes):
        cnt = [0] * 100
        ans = 0
        for a, b in dominoes:
            # encode the unordered pair (a,b) as a two‐digit key 0…99
            k = a * 10 + b if a <= b else b * 10 + a
            ans += cnt[k]
            cnt[k] += 1
        return ans
