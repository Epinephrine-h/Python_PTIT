class Student:
    def __init__(self, name, birth_day, point1, point2, point3):
        self.name = name
        self.birth_day = birth_day
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
    def __str__(self):
        total_point = self.point1 + self.point2 + self.point3
        return f"{self.name} {self.birth_day} {total_point:.1f}"
x = Student(
    input(),
    input(),
    float(input()),
    float(input()),
    float(input())
)
print(x)