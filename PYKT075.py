class Contact:
    def __init__(self, date, name, number):
        self.date = date.split()[-1]
        names = name.split()
        self.main_name = names[-1]
        self.sub_name = names[0]
        self.name = name
        self.number = number
    def __str__(self):
        return f"{self.name}: {self.number} {self.date}"
ls = []
data = []
with open("SOTAY.txt") as f:
    for x in f: data.append(x.strip())
idx = 0
while idx < len(data):
    date = data[idx]
    idx+=1
    while idx < len(data) and data[idx][:4] != "Ngay":
        ls.append(Contact(date, data[idx], data[idx+1]))
        idx+=2
ls.sort(key=lambda x : (x.main_name, x.sub_name))
with open("DIENTHOAI.txt", "w") as f:
    for x in ls:
        f.write(f"{x.name}: {x.number} {x.date}")
        f.write('\n')