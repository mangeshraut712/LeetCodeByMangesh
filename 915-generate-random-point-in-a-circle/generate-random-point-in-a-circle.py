from random import random as R
from math import pi, cos, sin, sqrt

class Solution:
    def __init__(self, r, x, y):
        self.r, self.x, self.y = r, x, y
    def randPoint(self):
        t = R() * 2 * pi
        d = sqrt(R()) * self.r
        return [self.x + d * cos(t), self.y + d * sin(t)]
