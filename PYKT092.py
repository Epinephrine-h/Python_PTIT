import sys
add = {1:1.5, 2:1, 3:0}
def get_name(raw_data):
    words = [word.title() for word in raw_data.split()]
    return " ".join(words)
class Candidate:
    def __init__(self, id, name, point, race, area):
        self.id = f"TS{id:02d}"
        self.name = get_name(name)
        self.point = point + add[area] if area in add else point
        self.race = race
        if self.race != "Kinh":     self.point+=1.5
        self.status = "Do" if self.point >= 20.5 else "Truot"
    def __str__(self):
        return f"{self.id} {self.name} {self.point:.1f} {self.status}"
input = sys.stdin.readline
n = int(input().strip())
lst = []
for i in range(n):

    x = Candidate(
        i + 1,
        input().strip(),
        float(input().strip()),
        input().strip(),
        int(input().strip())
    )
    lst.append(x)
lst.sort(key = lambda x : -x.point)
print(*lst, sep = '\n')
