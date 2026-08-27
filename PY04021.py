class Client:
    def __init__(self, id, name, start_time, end_time):
        self.id = id
        self.name = name 
        start_h, start_p = map(int, start_time.split(':'))
        end_h, end_p = map(int, end_time.split(':'))
        p = end_p - start_p
        h = end_h - start_h
        self.p = p if p >= 0 else p + 60
        self.h = h if p >= 0 else h - 1
        self.play_time = f"{self.h} gio {self.p} phut"
    def __str__(self):
        return f"{self.id} {self.name} {self.play_time}"
testcase = int(input())
lst = []
for _ in range(testcase):
    x = Client(
        input(),
        input(),
        input(),
        input()
    )
    lst.append(x)
lst.sort(key = lambda x : (-x.h, -x.p))
print(*lst, sep = '\n')