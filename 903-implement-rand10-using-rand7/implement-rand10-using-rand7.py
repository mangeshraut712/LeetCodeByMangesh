# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Generate a number in the range [1, 49] by combining two rand7() calls.
            # (rand7() - 1) * 7 gives a value in [0, 6] * 7 = [0, 42] in steps of 7.
            # Adding another rand7() (which is in [1, 7]) results in a value in [1, 49].
            r = (rand7() - 1) * 7 + rand7()

            # If the generated value 'r' is within the range [1, 40], it can be
            # uniformly mapped to the range [1, 10].
            if r <= 40:
                # Map the value from [1, 40] to [1, 10] using modulo and addition.
                # (r - 1) gives a value in [0, 39].
                # (r - 1) % 10 gives a value in [0, 9].
                # Adding 1 shifts the range to [1, 10].
                return (r - 1) % 10 + 1

            # If 'r' is in the range [41, 49], reject this value and repeat the process.
            # This ensures uniformity because each value in [1, 40] had an equal
            # probability of being generated and accepted.
