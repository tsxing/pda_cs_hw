t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    cows = list(input().strip())
    patches = ['.'] *n
    fed = [False] *n
    count = 0

    i = 0
    while i < n:
        if fed[i]:
            i += 1
            continue
        breed = cows[i]
        pos = min(i +k, n -1)
        while pos >= i and cows[pos] != breed:
            pos -= 1
        if pos < i:
            pos = min(i +k, n -1)

        patches[pos] = breed
        count += 1

        for j in range(max(0, pos -k), min(n, pos +k +1)):
            if cows[j] == breed:
                fed[j] = True
        i += 1

    print(count)
    print("".join(patches))
