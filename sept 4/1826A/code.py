t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans =-1
    for x in range(n+1):
        cnt = sum(1 for v in a if x >= v)
        if cnt ==n - x:
            ans =x
            break
    print(ans)


# works - sept 9
