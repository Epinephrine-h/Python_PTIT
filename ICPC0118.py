date = [19, 18, 20, 19, 20, 20, 22, 22, 22, 22, 22, 21]
zodiac = ["Ma Ket", "Bao Binh", "Song Ngu", "Bach Duong", "Kim Nguu", "Song Tu", "Cu Giai", "Su Tu", "Xu Nu", "Thien Binh", "Thien Yet", "Nhan Ma"]
#main
testcase = int(input())
for _ in range(testcase):
    day, month = map(int, input().split())
    print(zodiac[month - 1] if day <= date[month - 1] else zodiac[month % 12])