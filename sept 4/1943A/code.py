t = int(input()) # we did this in class so i j copied this code from my doc
for _ in range(t):
    n = int(input())
    f = [0] * (n + 1)
    arr = list(map(int, input().split()))
    for x in arr:
        f[x] += 1
    c = 0
    for i in range(n + 1):
        c += (f[i] == 1)
        if c == 2 or f[i] == 0:
            print(i)
            break
