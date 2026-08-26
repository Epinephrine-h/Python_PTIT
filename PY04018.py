subjects = {'A':"TOAN", 'B':"LY", 'C':"HOA"}
p = {1:2.0, 2:1.5, 3:1.0, 4:0.0}
class Candidate:
    def __init__(self, id, name, mc, point_1, point_2):
        self.id = f"GV{id:02d}"
        self.name = name
        self.major = subjects[mc[0]]
        self.priority = int(mc[1])
        self.point_1 = point_1
        self.point_2 = point_2
        self.total = self.point_1 * 2 + self.point_2 + p[self.priority]
        self.status = "LOAI" if self.total < 18.0 else "TRUNG TUYEN"
    def __str__(self):
        return f"{self.id} {self.name} {self.major} {self.total:.1f} {self.status}"
n = int(input())
lst = []
for idx in range(n):
    x = Candidate(
        idx + 1,
        input(),
        input(),
        float(input()),
        float(input())
    )
    lst.append(x)
lst.sort(key = lambda x : -x.total)
print(*lst, sep = '\n')