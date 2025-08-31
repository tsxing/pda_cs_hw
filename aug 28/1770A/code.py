t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    for bj in b:

        idx = a.index(min(a))
        a[idx] = bj

    print(sum(a))
