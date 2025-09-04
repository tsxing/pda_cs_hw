N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

used = [False] * N

def find(cow, N, a, b, used):
    if cow== N:  
        return 1
        
    cnt= 0
    for stall in range(N):
        if not used[stall] and a[cow]<= b[stall]:
            used[stall]= True
            cnt += find(cow+1, N, a, b, used)
            used[stall] = False
    return cnt

print(find(0, N, a, b, used))
