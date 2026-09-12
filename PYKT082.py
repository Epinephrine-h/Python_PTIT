def get_point(amount):
    corrects = [4, 6, 9, 12, 15, 19, 22, 26, 29, 32, 34, 36, 38, 40]
    points = [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0]
    for c, p in zip(corrects, points):
        if amount <= c:
            return p
class Student:
    def __init__(self, read, listen, speak, write):
        self.read = get_point(int(read))
        self.listen = get_point(int(listen))
        self.speak = speak
        self.write = write
        self.overall = (self.listen + self.read + self.speak + self.write) / 4 + 0.25
        self.overall = self.overall//0.5 * 0.5
    def __str__(self):
        return f"{self.overall:.1f}"
        
testcase = int(input())
ls = []
for _ in range(testcase):
    data = input().split()
    ls.append(Student(int(data[0]), int(data[1]), float(data[2]), float(data[3])))
print(*ls, sep = '\n')
