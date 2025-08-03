t = int(input())

def solve(a):
    for i in range(n):
        for j in range(i+2,n):
            if a[j]==a[i]:
                return True
    return False
            
    
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if solve(a):
        print("YES")
    else:
        print("NO")
    
                
