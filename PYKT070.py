subject = {}

class Session:
    def __init__(self, id, ids, idg, cap):
        self.id = id
        self.name = subject[ids][0]
        self.idg = idg
        self.cap = cap
        self.time = None
        self.date = None
        self.idr = None

    def __str__(self):
        return f"{self.date} {self.time} {self.idr} {self.name} {self.idg} {self.cap}"

def get_data(path):
    with open(path) as f:
        return [line.strip() for line in f.split()]
# Môn thi
data = get_data("MONTHI.in")
n = int(data[0])
idx = 1
for _ in range(n):
    ids, name, fmt = data[idx], data[idx+1], data[idx+2]
    idx += 3
    subject[ids] = (name, fmt)

# Ca thi: mã tự tăng từ C001, lưu theo mã
data = get_data("CATHI.in")
n = int(data[0])
idx = 1
slots = {}
for i in range(n):
    code = f"C{i+1:03d}"
    slots[code] = (data[idx], data[idx+1], data[idx+2])  # date, time, room
    idx += 3

# Lịch thi
data = get_data("LICHTHI.in")
n = int(data[0])
ls = []
for i in range(1, n + 1):
    s = data[i].split()
    ss = Session(s[0], s[1], s[2], s[3])
    ss.date, ss.time, ss.idr = slots[ss.id]
    ls.append(ss)

def key(x):
    d, m, y = x.date.split('/')
    return (y, m, d, x.time, x.id)

ls.sort(key=key)
print(*ls, sep='\n')