def get_id(unit, name):
    word = list(unit.split()) + list(name.split())
    id = [w[0] for w in word]
    return "".join(id)
def get_speed(time):
    h, m = map(int,time.split(":"))
    t = (h - 6) + m/60
    return 120/t
class Driver:
    def __init__(self, name, unit, time):
        self.name = name
        self.unit = unit
        self.id = get_id(unit, name)
        self.speed = get_speed(time)
    def __str__(self):
        return f"{self.id} {self.name} {self.unit} {round(self.speed)} Km/h"
testcase = int(input())
lst = []
for _ in range(testcase):
    x = Driver(
        input(),
        input(),
        input()
    )
    lst.append(x)
lst.sort(key = lambda x : -x.speed)
for x in lst:
    print(x)