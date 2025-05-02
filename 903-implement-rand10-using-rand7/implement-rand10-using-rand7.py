# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Generate a number in the range [0, 48] with uniform probability
            row = rand7()
            col = rand7()
            val = (row - 1) * 7 + (col - 1)

            # If the value is in the range [0, 39], we can map it to [1, 10]
            if val < 40:
                # Map the value to the range [1, 10]
                return (val % 10) + 1

            # If the value is in the range [40, 48], reject and repeat
