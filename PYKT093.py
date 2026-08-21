from math import ceil
def get_name(raw_data):
    clean_data = list(word.title() for word in raw_data.split())
    return " ".join(clean_data)
class Student:
    def __init__(self, id, name, p1, p2, p3):
        self.id = f"SV{id:02d}"
        self.name = get_name(name)
        self.average = (p1*3 + p2*3 + p3*2)/8
    def __str__(self):
        return f"{self.id} {self.name} {ceil(self.average*100)/100:.2f} {self.rank}"
n = int(input())
lst = []
for ith in range(n):
    x = Student(
        ith + 1,
        input(),
        int(input()),
        int(input()),
        int(input())
    )
    lst.append(x)
lst.sort(key = lambda x : (-x.average, x.id))
lst[0].rank = 1
for i in range(1, n):
    lst[i].rank = lst[i-1].rank if lst[i].average == lst[i-1].average else i + 1
for x in lst:
    print(x)