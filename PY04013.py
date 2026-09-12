def get_time(s, e):
    t1 = list(map(int, s.split(":")))
    t2 = list(map(int, e.split(":")))
    m, h = t2[1] - t1[1], t2[0] - t1[0]
    if m < 0:
        m+=60
        h-=1
    return h + m/60
class City:
    def __init__(self, id, name, s, e, r):
        self.id = f"T{id:02d}"
        self.name = name
        self.time = get_time(s, e)
        self.l = r
    def __str__(self):
        return f"{self.id} {self.name} {self.l/self.time:.2f}"
if __name__ == '__main__':
    m = {}
    n = int(input())
    id = 1
    for _ in range(n):
        name = input()
        s, e = input(), input()
        l = float(input())
        if name not in m:
            x = City(id, name, s, e, l)
            id+=1
            m[name] = x
        else:
            m[name].time+=get_time(s, e)
            m[name].l+=l
    for x in m.values():
        print(x)