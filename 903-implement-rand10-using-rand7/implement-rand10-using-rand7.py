class Solution:
    def rand10(self):
        r7 = rand7
        while (r := (r7() - 1) * 7 + r7()) > 40:
            pass
        return (r - 1) % 10 + 1
