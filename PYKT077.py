subjects = {}

class Session:
    def __init__(self, code, id, date, time, group):
        self.code = f"T{code:03d}"
        self.id = id
        self.sub_name = subjects[id]
        self.date = date
        self.day, self.month, self.year = map(int, date.split('/'))
        self.time = time
        self.h, self.p = map(int, time.split(':'))
        self.group = group
    def __str__(self):
        return f"{self.code} {self.id} {self.sub_name} {self.date} {self.time} {self.group}"

def solve():
    n, m = map(int, input().split())
    for s in range(n):
        id, name = input(), input()
        subjects[id] = name
    lst = []
    for idx in range(m):
        line = input().split()
        x = Session(idx + 1, line[0], line[1], line[2], line[3])
        lst.append(x)
    lst.sort(key = lambda x : (x.year, x.month, x.day, x.h, x.p, x.id))
    print(*lst, sep = '\n')
solve()