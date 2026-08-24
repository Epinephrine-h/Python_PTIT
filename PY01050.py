def solve():
    n = int(input())

    def gen_strings(a, b, c):
        cnt = {'A':a, 'B':b, 'C':c}
        total = a + b + c
        path = []
        res = []
        def backtrack():
            if len(path) == total:
                res.append(''.join(path))
                return
            for ch in ('A', 'B', 'C'):
                if cnt[ch] > 0:
                    cnt[ch]-=1
                    path.append(ch)
                    backtrack()
                    path.pop()
                    cnt[ch]+=1
        backtrack()
        return res

    for tmp_n in range(3, n + 1):
        amount = []
        for a in range(1, tmp_n // 3 + 1):
            for b in range(a, (tmp_n - a) // 2 + 1):
                c = tmp_n - a - b
                if c >= b:
                    amount.append((a, b, c))
        ans = []
        for a, b, c in amount:
            ans.extend(gen_strings(a, b, c))
        ans.sort()
        print(*ans, sep='\n')

solve()