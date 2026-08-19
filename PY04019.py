class Candidate:
    def __init__(self, name, point_1, point_2, order):
        self.name = name
        self.point_1 = point_1 if point_1 <= 10 else point_1/10
        self.point_2 = point_2 if point_2 <= 10 else point_2/10
        self.candidate_number = f"TS0{order}"
        self.average_point = (self.point_1 + self.point_2) / 2
    def __str__(self):
        if self.average_point < 5:   status = "TRUOT"
        elif self.average_point < 8: status = "CAN NHAC"
        elif self.average_point <= 9.5:   status = "DAT"
        else:   status = "XUAT SAC"
        return f"{self.candidate_number} {self.name} {self.average_point:.2f} {status}"
n = int(input())
candidate_list = []
for i in range(n):
    x = Candidate(
        input(),
        float(input()),
        float(input()),
        i + 1
    )
    candidate_list.append(x)
candidate_list.sort(key = lambda x : x.average_point, reverse = True)
for x in candidate_list:
    print(x)