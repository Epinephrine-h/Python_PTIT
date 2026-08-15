def HanoiTower(n, A, B, C):
    if n == 1:  
        print(A + ' -> ' + C)
        return
    HanoiTower(n - 1, A, C, B)
    HanoiTower(1, A, B, C)
    HanoiTower(n - 1, B, A, C)
HanoiTower(int(input()), 'A', 'B', 'C')