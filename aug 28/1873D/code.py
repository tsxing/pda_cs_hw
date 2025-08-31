t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    i = 0
    ans = 0
    while i < n:
        if s[i] == 'W':
            i += 1
        else:  
            ans += 1
            i += k  
    print(ans)
