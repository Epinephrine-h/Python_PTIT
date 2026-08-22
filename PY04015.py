fee_50 = 5_000
fee_100 = 12_500
class Client:
    def __init__(self, id, name, old_index, new_index):
        self.id = f"KH{id:02d}"
        self.name = name
        self.consumption = new_index - old_index
        if self.consumption <= 50:      self.fee = self.consumption * 100 * 1.02
        elif self.consumption <= 100:   self.fee = ((self.consumption - 50) * 150 +  fee_50) * 1.03
        else:                           self.fee = ((self.consumption - 100) * 200 + fee_100) * 1.05
    def __str__(self):
        return f"{self.id} {self.name} {round(self.fee)}"
n = int(input())
lst = []
for i in range(n):
    x = Client(
        i + 1,
        input(),
        int(input()),
        int(input())
    )
    lst.append(x)
lst.sort(key=lambda x : -x.fee)
print(*lst, sep = "\n")