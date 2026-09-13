class Team:
    def __init__(self, name, school):
        self.name = name
        self.school = school
class Contestant:
    def __init__(self, id, name, team_name, school):
        self.id = f"C{id:03d}"
        self.name = name
        self.team_name = team_name
        self.school = school
    def __str__(self):
        return f"{self.id} {self.name} {self.team_name} {self.school}"
n = int(input())
teams = {}
for i in range(n):
    id = f"Team{i+1:02d}"
    name = input()
    school = input()
    teams[id] = Team(name, school)
m = int(input())
ls = []
for i in range(m):
    name = input()
    t = input()
    ls.append(Contestant(i+1, name, teams[t].name, teams[t].school))
ls.sort(key=lambda x: x.name)
print(*ls, sep = '\n')