fee = {("Xe_con", 5): 10000, ("Xe_con", 7): 15000, ("Xe_tai", 2): 20000, ("Xe_khach", 29): 50000, ("Xe_khach", 45): 70000}
statistics = {}
n = int(input())
for _ in range(n):
    vrp, type, seat, direct, date = input().split()
    seat = int(seat)
    if direct == "OUT":     continue
    if date not in statistics:
        statistics[date] = fee[(type, seat)]
    else:
        statistics[date]+=fee[(type, seat)]
for date, money in statistics.items():
    print(date, ": ", money, sep = "")

