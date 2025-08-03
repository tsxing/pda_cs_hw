import sys
sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")

n = int(input())
log=[]
for _ in range(n):
    r = int(input())
    log.append(r)
    
ans = 10000000000000
for start_door in range(n):
    dist = 0
    tot = sum(log) # total cows
    remaining = tot #cows remaining
    for r in range(n):
        remaining-= log[(start_door+r)%n]
        dist += remaining
    ans = min(dist,ans)
print(ans)
