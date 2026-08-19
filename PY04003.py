import math
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def simplify(self):
        divisor = math.gcd(self.numerator, self.denominator)
        self.numerator //= divisor
        self.denominator //= divisor
        print(f"{self.numerator}/{self.denominator}")
x, y = map(int, input().split())
f = Fraction(x, y)
f.simplify()