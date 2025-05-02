class Solution:
    def rand10(self):
        r7 = rand7
        while True:
            r = (r7() - 1) * 7 + r7()
            if r <= 40:
                return (r - 1) % 10 + 1
