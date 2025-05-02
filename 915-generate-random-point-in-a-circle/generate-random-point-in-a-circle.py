import random
import math
from typing import List

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        """
        Initializes the Solution object with circle parameters.

        Args:
            radius: The radius of the circle.
            x_center: The x-coordinate of the circle's center.
            y_center: The y-coordinate of the circle's center.
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        """
        Generates a uniform random point inside the circle.

        Uses polar coordinates to ensure uniform distribution.

        Returns:
            A list [x, y] representing the random point.
        """
        # Generate a random distance from the center.
        # To ensure uniform distribution of points, the square of the radius
        # should be uniformly distributed. So we take the square root of a
        # uniform random number between 0 and 1, and multiply by the radius.
        r = self.radius * math.sqrt(random.random())

        # Generate a random angle between 0 and 2*pi.
        theta = random.uniform(0, 2 * math.pi)

        # Convert polar coordinates (r, theta) to Cartesian coordinates (x, y)
        # relative to the center of the circle.
        delta_x = r * math.cos(theta)
        delta_y = r * math.sin(theta)

        # Calculate the final coordinates by adding the center coordinates.
        x = self.x_center + delta_x
        y = self.y_center + delta_y

        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
