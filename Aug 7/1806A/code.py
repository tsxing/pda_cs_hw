t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    if d>=b and d-b>=c-a:
        print((d-b)+(a+d-b-c))
    else:
        print(-1)
    
