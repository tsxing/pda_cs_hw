import sys
sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

N = int(input())
log=[]
for _ in range(N):
    s,t,b=map(int,input().split())
    log.append([s,t,b])

ans = 0
for t in range(1,1001):
    amt = 0
    for cow in range(N):
        if log[cow][0] <=t<=log[cow][1]:
            amt+=log[cow][2]
            
    ans = max(ans,amt)
print(ans)
    
