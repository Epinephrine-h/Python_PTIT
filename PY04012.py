
class Student:
    def __init__(self, id, name, clan):
        self.id = id
        self.name = name
        self.clan = clan
        self.point = 10
        self.status = ""
    def __str__(self):
        return f"{self.id} {self.name} {self.clan} {self.point} {self.status}"
def solve():
    testcase = int(input())
    lst = []
    for _ in range(testcase):
        x = Student(input(), input(), input())
        lst.append(x)
    for _ in range(testcase):
        id, data = input().split()
        for x in lst:
            if x.id == id:
                for s in data:
                    if s == 'v':    x.point-=2
                    elif s == 'm':  x.point-=1
    for x in lst:
        if x.point <= 0: 
            x.point = 0   
            x.status = "KDDK"
        print(x)
solve()