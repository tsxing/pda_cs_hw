import sys
sys.stdin = open("angry.in", "r")
sys.stdout = open("angry.out", "w")


def right_most(start):
    last = start
    r = 1
    while True:
        new = last
        while 0 <= new + 1 < N and abs(bales[new + 1] - bales[last]) <= r:
            new += 1
        if new == last:
            break
        last = new
        r += 1
    return last

def left_most(start):
    last = start
    r = 1
    while True:
        new = last
        while 0 <= new - 1 < N and abs(bales[new -1] - bales[last]) <= r:
            new-=1
        if new == last:
            break
        last = new
        r += 1
    return last

N = int(input())
bales=[]
for _ in range(N):
    x =int(input())
    bales.append(x)

bales.sort()
ans = 1

for i in range(N):
    right = right_most(i)
    left = left_most(i)
    explode = right - left + 1
    if explode > ans:
        ans = explode

print(ans)
