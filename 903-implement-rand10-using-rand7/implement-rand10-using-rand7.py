class Solution:
    def rand10(self):
        while True:
            r = (rand7() - 1) * 7 + rand7()
            if r <= 40:
                return (r - 1) % 10 + 1
