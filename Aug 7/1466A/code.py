t = int(input())

def solve(a):
    cnt = 0
    thing = []
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            thing.append(a[i]-a[j])
    return len(set(thing))
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(a))
