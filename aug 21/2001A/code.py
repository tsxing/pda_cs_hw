def solve(a):
    n = len(a)
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1

    max_f = max(freq.values())
    print(n - max_f)

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    solve(a)
