t = int(input())
for _ in range(t):
    x1,y1,x2,y2 = map(int, input().split())
    if (x2-x1) ==0:
        print(abs(y2-y1))
    elif (y2-y1) ==0:
        print(abs(x2-x1))
    else:
        print(abs(x2-x1) +abs(y2-y1) + 2)
