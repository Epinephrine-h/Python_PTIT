import sys
import bisect
def main():
    antiprimes = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 
        15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 
        554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 
        10810800, 14414400]
    testcase = int(input())
    t = 0
    for line in sys.stdin:
        n = int(line)
        pos = bisect.bisect_left(antiprimes, n)
        print(antiprimes[pos])
        t+=1
        if t == testcase:   break
if __name__ == '__main__':# Add this fucking line unless you wanna enjoy Time Limit Exceeded
    main()
"""use this to find antiprimes
candidates = [(1,1)]
LIMIT = 15_000_000
def solve():
    def dfs(idx, value, div_cnt, max_e):
        if idx == len(prime):
            return
        p, v = prime[idx], value
        for e in range(1, max_e + 1):
            v *= p
            if v > LIMIT:
                break
            dc = div_cnt * (e + 1)
            candidates.append((v, dc))
            dfs(idx+1, v, dc, e)
    dfs(0,1,1,25)
    candidates.sort()
    antiprime = []
    best = 0
    for v, dc in candidates:
        if dc > best:
            best = dc
            antiprime.append(v)
    print(antiprime)
solve()"""