dep = {}
table = {
    'A':(10, 12, 14, 20),
    'B':(10, 11, 13, 16),
    'C':(9, 10, 12, 14),
    'D':(8, 9, 11, 13)
}
def get_coef(x):
    t, year = x[0], int(x[1:])
    if year <= 3:   return table[t][0]
    elif year <= 8:     return table[t][1]
    elif year <= 15:    return table[t][2]
    return table[t][3]
class Employee:
    def __init__(self, id, name, base_salary, day):
        self.id = id
        self.name = name
        self.department = dep[id[-2:]]
        coef = get_coef(id[:-2])
        self.total = coef * day * base_salary * 1000
    def __str__(self):
        return f"{self.id} {self.name} {self.department} {self.total}"
n = int(input())
for _ in range(n):
    s = input().split()
    idd = s[0]
    named = ' '.join(s[1:])
    dep[idd] = named
m = int(input())
for _ in range(m):
    print(Employee(input(), input(), int(input()), int(input())))