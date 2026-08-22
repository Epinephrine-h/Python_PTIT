class Subject:
    def __init__(self, code, name, form):
        self.code = code
        self.name = name
        self.form = form
    def __str__(self):
        return f"{self.code} {self.name} {self.form}"
testcase = int(input())
lst = []
for _ in range(testcase):
    x = Subject(
        input(),
        input(),
        input()
    )
    lst.append(x)
lst.sort(key = lambda x : x.code)
print(*lst, sep = '\n')
