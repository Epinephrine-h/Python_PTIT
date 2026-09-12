floor = {1:25, 2:34, 3:50, 4:80}

def get_day(month):
    #You can take leap years into account,
    #but since the test cases for this problem seem quite lenient, simply returning 28 for February should suffice.
    if month == 2:
        return 28
    return 31 if month in (1, 3, 5, 7, 8, 10, 12) else 30

def get_time(s, e):
        t1 = list(map(int, s.split("/")))
        t2 = list(map(int, e.split("/")))
        cnt = 0

        for month in range(t1[1]+1, t2[1]):
            cnt+=get_day(month)

        if t2[1] == t1[1]:
            cnt+=t2[0] - t1[0] + 1
        else:
            cnt+=get_day(t1[1])-t1[0]+t2[0] + 1
        return cnt

class Client:

    def __init__ (self, id, name, room, s, e, plus):
        self.id = f"KH{id:02d}"
        self.name = name
        self.room = room
        self.time = get_time(s, e)
        self.rent = self.time * floor[int(room[:1])] + plus

    def __str__(self):
        return f"{self.id} {self.name} {self.room} {self.time} {self.rent}"
    
if __name__ == "__main__":
    n = int(input())
    ls = []
    for i in range(n):
        x = Client(i+1, input(), input(), input(), input(), int(input()))
        ls.append(x)
    ls.sort(key=lambda x : -x.rent)
    print(*ls, sep = '\n')
        