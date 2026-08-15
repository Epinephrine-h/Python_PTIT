n = int(input())
student = {}
for i in range(n):
    name = input()
    correct, submit = map(int, input().split())
    student[name] = {"correct": correct, "submit" : submit}
ans = sorted(student,
    key = lambda name : (-student[name]["correct"], student[name]["submit"])
)
for name in ans:
    print(name, student[name]["correct"], student[name]["submit"])