def solve(a):
    # compress same elements
    b = [a[0]]
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            b.append(a[i])

    m = len(b)
    cnt = 0
    
    for i in range(m):
        left_ok , right_ok = False, False
        if i==0 or b[i-1]>b[i]:
            left_ok = True
        if i==m-1 or b[i+1]>b[i]:
            right_ok = True
        
        if left_ok and right_ok:
            cnt += 1

    print("YES" if cnt == 1 else "NO")

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    solve(a)
