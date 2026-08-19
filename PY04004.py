import math
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def simplify(self):
        divisor = math.gcd(self.denominator, self.numerator)
        self.numerator //= divisor
        self.denominator //= divisor
        return self
    def add(self, other):
        new_num = self.numerator*other.denominator + other.numerator*self.denominator
        new_den = self.denominator*other.denominator
        res = Fraction(new_num, new_den)
        res.simplify()
        return res
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
x, y, z, t = map(int, input().split())
f1, f2 = Fraction(x, y), Fraction(z, t)
f3 = f1.add(f2)
print(f3)