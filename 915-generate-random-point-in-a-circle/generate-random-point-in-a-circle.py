import random, math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r, self.x, self.y = radius, x_center, y_center

    def randPoint(self) -> List[float]:
        t = random.random() * 2 * math.pi
        d = math.sqrt(random.random()) * self.r
        return [self.x + d * math.cos(t), self.y + d * math.sin(t)]
