type_dict = {}
class Film:
    def __init__(self, idx, type_id, date, name, epi):
        self.id = f"P{idx:03d}"
        self.type = type_dict[type_id]
        self.date = date
        self.name = name
        self.epi = epi
        self.day, self.month, self.year = map(int, date.split('/'))
    def __str__(self):
        return f"{self.id} {self.type} {self.date} {self.name} {self.epi}"
n, m = map(int, input().split())
for i in range(n):
    c, t = f"TL{i+1:03d}", input()
    type_dict[c] = t
lst = []
for idx in range(1, m + 1):
    x = Film(
        idx,
        input(),
        input(),
        input(),
        int(input())
    )
    lst.append(x)
lst.sort(key = lambda x : (x.year, x.month, x.day, x.name, -x.epi))
print(*lst, sep = '\n')