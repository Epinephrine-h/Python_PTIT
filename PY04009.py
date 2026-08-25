class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def add(self, other):
        r = self.re + other.re
        i = self.im + other.im
        return ComplexNumber(r, i)
    def mul(self, other):
        r = self.re * other.re - self.im * other.im
        i = self.re * other.im + self.im * other.re
        return ComplexNumber(r, i)
    def __str__(self):
        sign = '-' if self.im < 0 else '+'
        return f"{self.re} {sign} {abs(self.im)}i"
testcase = int(input())
for _ in range(testcase):
    x, y, z, t = map(int, input().split())
    A, B = ComplexNumber(x, y), ComplexNumber(z, t)
    tmp = A.add(B)
    print(tmp.mul(A), tmp.mul(tmp), sep = ", ")