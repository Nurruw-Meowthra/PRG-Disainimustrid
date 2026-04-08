from cmath import sqrt

class DiscriminantStrategy:
    def calculate_discriminant(self, a, b, c):
        pass

class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b**2 - 4*a*c

class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        discriminant = b**2 - 4*a*c
        return discriminant if discriminant >= 0 else float('nan')

class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        discriminant = self.strategy.calculate_discriminant(a, b, c)
        root_d = sqrt(discriminant)
        x1 = (-b + root_d) / (2*a)
        x2 = (-b - root_d) / (2*a)
        return x1, x2