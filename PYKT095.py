t = {'A':100, 'B':500, 'C':200}
def get_name(raw_data):
    words = [word.title() for word in raw_data.split()]
    return " ".join(words)
class Resident:
    def __init__(self, id, name, information):
        self.id = f"KH{id:02d}"
        self.name = get_name(name)
        data = information.split()
        self.typ = data[0]
        self.en = int(data[2]) - int(data[1])
        #calculate fee
        over = self.en - t[self.typ]
        self.fee = self.en * 450 if over < 0 else t[self.typ] * 450
        self.over_fee = over *1000 if over > 0 else 0
        self.vat = self.over_fee // 20
        self.total_fee = self.fee+self.over_fee+self.vat
    def __str__(self):
        return f"{self.id} {self.name} {self.fee} {self.over_fee} {self.vat} {self.total_fee}"
n = int(input())
lst = []
for i in range(n):
    x = Resident(
        i + 1,
        input(),
        input()
    )
    lst.append(x)
lst.sort(key=lambda x: -x.total_fee)
print(*lst, sep = '\n')
