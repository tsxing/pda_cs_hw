N = int(input())
p = [int(x) for x in input().split()]
cnt = 0

for i in range(N):
    total = 0
    for j in range(i, N):
        total +=p[j]
        length =j-i+1
        if total%length != 0:
            continue
        avg = total // length
        if avg in p[i:j+1]:
            cnt += 1

print(cnt)
