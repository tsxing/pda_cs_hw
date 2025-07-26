#circle of students

def solve(a):
    n = len(a)
    if n == 1:
        return True
 
    for start in range(n):
        inc = True
        dec = True
        for i in range(n - 1):
            cur = a[(start + i) % n]
            nex = a[(start + i + 1) % n]
            if nex <= cur:
                inc = False
            if nex >= cur:
                dec = False
        if inc or dec:
            return True
    return False
 
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if solve(a):
        print("YES")
    else:
        print("NO")
