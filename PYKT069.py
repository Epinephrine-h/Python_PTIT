class Session:
    def __init__(self, order, date, time, room):
        self.order = f"C{order:03d}"
        self.date = date
        self.time = time
        self.day, self.month, self.year = map(int, date.split('/'))
        self.h, self.m = map(int, time.split(':'))
        self.room = room
    def __str__(self):
        return f"{self.order} {self.date} {self.time} {self.room}"

with open("CATHI.in") as f:
    data = f.read().split()
    n = int(data[0])
    idx = 1
    lst = []
    for i in range(n):
        x = Session(
            i + 1,
            data[idx],
            data[idx+1],
            data[idx+2]
        )
        idx+=3
        lst.append(x)
    lst.sort(key = lambda x : (x.year, x.month, x.day, x.h, x.m, x.order))
print(*lst, sep = '\n')
